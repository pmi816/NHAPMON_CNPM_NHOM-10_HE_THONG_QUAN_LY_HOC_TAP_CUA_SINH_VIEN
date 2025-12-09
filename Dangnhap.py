# Giả lập dữ liệu người dùng trong hệ thống
users_db = {
    "user@gmail.com": {
        "password": "123456",
        "role": "user",
        "failed_attempts": 0,
        "locked": False
    },
    "admin@gmail.com": {
        "password": "admin123",
        "role": "admin",
        "failed_attempts": 0,
        "locked": False
    }
}

def login(email, password):
    # Kiểm tra email tồn tại
    if email not in users_db:
        return "❌ Email không tồn tại!"

    user = users_db[email]

    # Kiểm tra tài khoản có bị khóa không
    if user["locked"]:
        return "🔒 Tài khoản đã bị khóa do nhập sai quá 5 lần!"

    # Kiểm tra mật khẩu
    if password == user["password"]:
        # Reset số lần sai sau khi đăng nhập đúng
        user["failed_attempts"] = 0  
        role = user["role"]
        
        # Điều hướng theo vai trò
        if role == "admin":
            return "✅ Đăng nhập thành công! Điều hướng đến trang Admin."
        else:
            return "✅ Đăng nhập thành công! Điều hướng đến trang Người dùng."

    # Nếu mật khẩu sai → tăng biến đếm
    user["failed_attempts"] += 1

    # Nếu sai 5 lần → khóa tài khoản
    if user["failed_attempts"] >= 5:
        user["locked"] = True
        return "🔒 Sai quá 5 lần! Tài khoản đã bị khóa tạm thời."

    return f"❌ Sai mật khẩu! Bạn đã nhập sai {user['failed_attempts']} lần."


# ===========================
# Ví dụ chạy thử
# ===========================

print(login("user@gmail.com", "123456"))        # đúng
print(login("user@gmail.com", "sai"))           # sai
print(login("user@gmail.com", "sai"))           # sai tiếp
