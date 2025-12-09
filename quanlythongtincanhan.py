# ==========================
# GIẢ LẬP DỮ LIỆU NGƯỜI DÙNG
# ==========================

user_info = {
    "name": "Nguyen Van A",
    "email": "user@gmail.com",
    "phone": "0123456789",
    "password": "123456"
}

# Dữ liệu toàn hệ thống để kiểm tra trùng
system_emails = {"user@gmail.com", "admin@gmail.com"}
system_phones = {"0123456789", "0987654321"}


# ==========================
# CÁC CHỨC NĂNG
# ==========================

def update_phone_email():
    new_phone = input("Nhập số điện thoại mới: ")
    new_email = input("Nhập email mới: ")

    # Kiểm tra trùng email hoặc số điện thoại
    if new_phone in system_phones or new_email in system_emails:
        return "❌ Số điện thoại hoặc email đã tồn tại trong hệ thống!"

    # Cập nhật
    user_info["phone"] = new_phone
    user_info["email"] = new_email

    # Lưu vào hệ thống
    system_phones.add(new_phone)
    system_emails.add(new_email)

    return "✅ Cập nhật số điện thoại/email thành công!"


def change_password():
    old_pw = input("Nhập mật khẩu cũ: ")

    if old_pw != user_info["password"]:
        return "❌ Mật khẩu cũ không đúng!"

    new_pw = input("Nhập mật khẩu mới: ")
    user_info["password"] = new_pw

    return "✅ Đổi mật khẩu thành công!"


def edit_name():
    new_name = input("Nhập họ tên mới: ")
    user_info["name"] = new_name
    return "✅ Cập nhật họ tên thành công!"


def show_success():
    return f"""
🎉 THÔNG TIN ĐÃ ĐƯỢC CẬP NHẬT 🎉
---------------------------------
Họ tên: {user_info['name']}
Email: {user_info['email']}
Số điện thoại: {user_info['phone']}
"""


# ==========================
# MENU CHÍNH
# ==========================

def menu():
    while True:
        print("\n=== QUẢN LÝ THÔNG TIN CÁ NHÂN ===")
        print("1. Cập nhật số điện thoại / email")
        print("2. Kiểm tra trùng thông tin")
        print("3. Thay đổi mật khẩu")
        print("4. Chỉnh sửa họ tên")
        print("5. Hiển thị thông tin sau cập nhật")
        print("6. Thoát")

        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            print(update_phone_email())
        elif choice == "2":
            print("📌 Email hiện có:", system_emails)
            print("📌 Số điện thoại hiện có:", system_phones)
        elif choice == "3":
            print(change_password())
        elif choice == "4":
            print(edit_name())
        elif choice == "5":
            print(show_success())
        elif choice == "6":
            print("👋 Thoát chương trình.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ! Vui lòng nhập từ 1-6.")


# Chạy chương trình
menu()
