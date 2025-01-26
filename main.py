def get_unique_names(names_list):
    """Returns a list of unique names sorted alphabetically"""
    if not isinstance(names_list, list):
        raise TypeError("Input must be a list")
    return sorted(list(set(names_list)))

def calculate_average_grade(grades):
    """Calculates the average grade from a dictionary of subjects and grades"""
    if not isinstance(grades, dict):
        raise TypeError("Input must be a dictionary")
    if not grades:
        raise ValueError("Grades dictionary cannot be empty")
    return sum(grades.values()) / len(grades)

def get_course_duration(course_name):
    """Returns the duration in months for a given course"""
    courses = {
        'python': 2,
        'java': 3,
        'javascript': 2,
        'php': 3,
        'c++': 4
    }
    if not isinstance(course_name, str):
        raise TypeError("Course name must be a string")
    course_name = course_name.lower()
    if course_name not in courses:
        raise ValueError(f"Course '{course_name}' not found")
    return courses[course_name]