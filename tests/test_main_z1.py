import pytest
from main import get_unique_names, calculate_average_grade, get_course_duration

# Задача №1 unit-tests
# Напишите тесты на любые 3 задания из модуля «Основы языка программирования Python». Используйте своё решение домашнего задания.
#
# При написании тестов не забывайте использовать параметризацию.
#
# Рекомендации по тестам: если у вас в функциях информация выводилась (print), то теперь её лучше возвращать (return), чтобы можно было протестировать.

@pytest.mark.parametrize("input_list, expected_output", [
    (["John", "Mary", "John", "Peter"], ["John", "Mary", "Peter"]),
    ([], []),
    (["A", "a", "B", "b"], ["A", "B", "a", "b"]),
    (["Test", "test", "TEST"], ["TEST", "Test", "test"])
])
def test_get_unique_names(input_list, expected_output):
    assert get_unique_names(input_list) == expected_output

def test_get_unique_names_type_error():
    with pytest.raises(TypeError):
        get_unique_names("not a list")

@pytest.mark.parametrize("input_dict, expected_output", [
    ({"Math": 90, "English": 85, "Science": 95}, 90.0),
    ({"Programming": 100}, 100.0),
    ({"A": 0, "B": 100}, 50.0)
])
def test_calculate_average_grade(input_dict, expected_output):
    assert calculate_average_grade(input_dict) == expected_output

def test_calculate_average_grade_errors():
    with pytest.raises(TypeError):
        calculate_average_grade([1, 2, 3])
    with pytest.raises(ValueError):
        calculate_average_grade({})

@pytest.mark.parametrize("course_name, expected_duration", [
    ("python", 2),
    ("JAVA", 3),
    ("JavaScript", 2),
    ("PHP", 3),
    ("C++", 4)
])
def test_get_course_duration(course_name, expected_duration):
    assert get_course_duration(course_name) == expected_duration

def test_get_course_duration_errors():
    with pytest.raises(TypeError):
        get_course_duration(123)
    with pytest.raises(ValueError):
        get_course_duration("invalid_course")

if __name__ == "__main__":
    pytest.main(["-v"])
