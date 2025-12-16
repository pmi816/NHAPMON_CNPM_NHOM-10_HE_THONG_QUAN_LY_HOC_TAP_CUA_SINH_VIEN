import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def is_duplicate_email(new_email: str, students: list) -> bool:
    for s in students:
        if s.get("email") == new_email:
            return True
    return False


def is_duplicate_phone(new_phone: str, students: list) -> bool:
    for s in students:
        if s.get("phone") == new_phone:
            return True
    return False


def check_duplicate_on_update(student_id: str, new_email: str, new_phone: str, students: list) -> bool:
    for s in students:
        if s.get("id") != student_id:
            if s.get("email") == new_email or s.get("phone") == new_phone:
                return True
    return False
