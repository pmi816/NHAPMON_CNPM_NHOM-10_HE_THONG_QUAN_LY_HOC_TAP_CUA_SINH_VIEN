import json
import os
import time

STUDENT_FILE = "students.json"
LOCK_TIME = 60  # khóa tạm thời 60 giây (bạn có thể đổi)

# ----------------------------------------
# Load dữ liệu sinh viên
# ----------------------------------------
def load_students():
    if not os.path.exists(STUDENT_FILE):
        return {}
    with open(STUDENT_FILE, "r") as f:
        return json.load(f)

# ----------------------------------------
# Lưu dữ liệu sinh viên
# ----------------------------------------
def save_students(data):
    with open(STUDENT_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ----------------------------------------
# Hàm đăng nhập theo User Story
# ----------------------------------------
def login():
    print("===== ĐĂNG NHẬP HỆ THỐNG =====")

    email = input("Nhập email: ").strip()
    password = input("Nhập mật khẩu: ").strip()

    students = load_students()

    # Kiểm tra email có tồn tại không
    if email not in students:
        print("Email không tồn tại!")
        return

    user = students[email]

    # Kiểm tra khóa tạm thời
    if user.get("locked_until", 0) > time.time():
        wait = int(user["locked_until"] - time.time())
        print(f"Tài khoản đã bị khóa. Vui lòng thử lại sau {wait} giây.")
        return

    # Nếu mật khẩu sai
    if password != user["password"]:
        user["failed_attempts"] = user.get("failed_attempts", 0) + 1

        if user["failed_attempts"] >= 5:
            user["locked_until"] = time.time() + LOCK_TIME
            print("Nhập sai 5 lần! Tài khoản bị khóa tạm thời 60 giây.")
        else:
            print(f"Sai mật khẩu! Bạn còn {5 - user['failed_attempts']} lần thử.")

        save_students(students)
        return

    # Đăng nhập thành công
    print("Đăng nhập thành công!")

    # Reset attempts
    user["failed_attempts"] = 0
    user["locked_until"] = 0
    save_students(students)

    # Chuyển hướng theo vai trò
    role = user.get("role", "student")

    if role == "admin":
        print("➡ Chuyển hướng đến TRANG ADMIN")
    elif role == "student":
        print("➡ Chuyển hướng đến TRANG SINH VIÊN")
    else:
        print(f"➡ Chuyển hướng đến TRANG: {role.upper()}")


# Chạy
login()
