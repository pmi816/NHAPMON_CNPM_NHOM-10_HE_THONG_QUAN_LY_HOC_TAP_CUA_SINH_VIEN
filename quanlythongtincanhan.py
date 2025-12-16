# quanlythongtincanhan.py

# ============================================
# PHẦN KHAI BÁO DATABASE (tùy bạn tự cài đặt)
# Có thể dùng: dictionary, JSON file, SQL...
# ============================================

# users = {}  # bạn tự tạo sau


# ============================================
# 1. Cập nhật thông tin cá nhân
# ============================================
def cap_nhat_thong_tin(user_id, full_name, email, phone):
    """
    TODO: Tự triển khai
    - Kiểm tra user tồn tại
    - Kiểm tra email trùng
    - Kiểm tra số điện thoại trùng
    - Cập nhật thông tin
    - Lưu lại database
    - Trả về thông báo thành công
    """
    pass


# ============================================
# 2. Đổi mật khẩu
# ============================================
def doi_mat_khau(user_id, old_password, new_password):
    """
    TODO: Tự triển khai
    - Kiểm tra user tồn tại
    - Kiểm tra mật khẩu cũ
    - Cập nhật mật khẩu mới
    - Lưu lại database
    - Trả về thông báo thành công
    """
    pass


# ============================================
# 3. Tạo user mới (phục vụ thêm dữ liệu)
# ============================================
def tao_user(full_name, email, phone, password):
    """
    TODO: Tự triển khai
    - Tạo user ID mới
    - Kiểm tra trùng email/phone nếu cần
    - Lưu user vào database
    - Trả về ID
    """
    pass


# ============================================
# 4. Menu chạy chính (tùy chọn)
# ============================================
def menu():
    """
    TODO: Tự triển khai nếu bạn muốn giao diện console
    """
    pass


# ============================================
# CHẠY CHƯƠNG TRÌNH
# ============================================
if __name__ == "__main__":
    menu()   # hoặc thay đổi theo ý bạn
