import requests
import unittest
import os
from time import sleep

# Задача №2 Автотест API Яндекса
# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
#
# Пример положительных тестов:
#
# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.

class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.token = os.getenv('YANDEX_DISK_TOKEN')  # требуется укзать свой токен в переменных среды
                                                     # Установите свой токен Yandex.Disk в качестве переменной среды
                                                     # export YANDEX_DISK_TOKEN='your_token_here'
        if not self.token:
            raise ValueError("Пожалуйста, установите переменную окружения YANDEX_DISK_TOKEN")

        self.base_url = "https://cloud-api.yandex.net/v1/disk"
        self.headers = {
            "Authorization": f"OAuth {self.token}",
            "Content-Type": "application/json"
        }
        self.test_folder_name = "test_folder"

    def tearDown(self):
        # Очистка: удалим тестовую папку, если она существует
        self._delete_folder(self.test_folder_name)

    def _delete_folder(self, folder_name):
        url = f"{self.base_url}/resources"
        params = {"path": folder_name, "permanently": True}
        requests.delete(url, headers=self.headers, params=params)
        sleep(1)  # Ожидаем завершения удаления

    def _check_folder_exists(self, folder_name):
        url = f"{self.base_url}/resources"
        params = {"path": folder_name}
        response = requests.get(url, headers=self.headers, params=params)
        return response.status_code == 200

    def test_create_folder_success(self):
        """Проверка успешного создания папки"""
        url = f"{self.base_url}/resources"
        params = {"path": self.test_folder_name}

        # Создаем папку
        response = requests.put(url, headers=self.headers, params=params)

        # Код статуса ответа на утверждение - 201 (создан)
        self.assertEqual(response.status_code, 201)

        # Убедимся, что папка существует
        self.assertTrue(self._check_folder_exists(self.test_folder_name))

    def test_create_existing_folder(self):
        """Протестируем создание папки, которая уже существует"""
        url = f"{self.base_url}/resources"
        params = {"path": self.test_folder_name}

        # Создаем папку в первый раз
        requests.put(url, headers=self.headers, params=params)
        sleep(1)  # Wait for creation to complete

        # Пробуем создать ту же папку еще раз
        response = requests.put(url, headers=self.headers, params=params)

        # Код состояния ответа на утверждение - 409 (конфликт)
        self.assertEqual(response.status_code, 409)

    def test_create_folder_invalid_token(self):
        """Протестируем создание папки с недопустимым токеном"""
        url = f"{self.base_url}/resources"
        params = {"path": self.test_folder_name}
        headers = {
            "Authorization": "OAuth invalid_token",
            "Content-Type": "application/json"
        }

        response = requests.put(url, headers=headers, params=params)

        # Код состояния ответа на запрос - 401 (несанкционированный)
        self.assertEqual(response.status_code, 401)

    def test_create_folder_invalid_name(self):
        """Протестируем создание папки с недопустимыми символами в названии"""
        invalid_folder_name = "test/\\?*:|\"<>"
        url = f"{self.base_url}/resources"
        params = {"path": invalid_folder_name}

        response = requests.put(url, headers=self.headers, params=params)

        # Код состояния ответа Assert - 400 (неверный запрос)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
