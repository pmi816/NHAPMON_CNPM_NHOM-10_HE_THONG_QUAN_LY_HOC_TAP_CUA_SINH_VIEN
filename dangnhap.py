import json
import time
from datetime import datetime, timedelta

class LoginSystem:
    def __init__(self):
        self.users_db = "users.json"
        self.load_users()
    
    def load_users(self):
        """Tải dữ liệu người dùng từ file JSON"""
        try:
            with open(self.users_db, 'r', encoding='utf-8') as f:
                self.users = json.load(f)
        except FileNotFoundError:
            # Tạo dữ liệu mẫu nếu file không tồn tại
            self.users = {
                "admin@example.com": {
                    "password": "admin123",
                    "role": "admin",
                    "failed_attempts": 0,
                    "locked_until": None,
                    "last_login": None
                },
                "user@example.com": {
                    "password": "user123",
                    "role": "user",
                    "failed_attempts": 0,
                    "locked_until": None,
                    "last_login": None
                }
            }
            self.save_users()
    
    def save_users(self):
        """Lưu dữ liệu người dùng vào file JSON"""
        with open(self.users_db, 'w', encoding='utf-8') as f:
            json.dump(self.users, f, indent=2, ensure_ascii=False)
    
    def format_last_login(self, last_login):
        """Định dạng thời gian đăng nhập cuối"""
        if not last_login:
            return "Chưa đăng nhập"
        
        # Kiểm tra nếu đã là chuỗi "Chưa đăng nhập"
        if isinstance(last_login, str) and ("Chua dāng nhập" in last_login or "Chưa đăng nhập" in last_login):
            return "Chưa đăng nhập"
        
        try:
            # Thử parse theo ISO format
            if isinstance(last_login, str):
                last_login = last_login.replace('Z', '+00:00')
                dt = datetime.fromisoformat(last_login)
                return dt.strftime('%d/%m/%Y %H:%M')
            else:
                return "Chưa đăng nhập"
        except (ValueError, TypeError):
            # Nếu không parse được, trả về nguyên bản
            return "Chưa đăng nhập"
    
    def is_account_locked(self, email):
        """Kiểm tra tài khoản có bị khóa không"""
        if email in self.users:
            user = self.users[email]
            if user["locked_until"]:
                lock_time = datetime.fromisoformat(user["locked_until"].replace('Z', '+00:00'))
                if datetime.now() < lock_time:
                    remaining = lock_time - datetime.now()
                    return f"Tài khoản bị khóa đến {lock_time.strftime('%H:%M:%S')} " \
                           f"(Còn lại: {int(remaining.total_seconds()//60)} phút {int(remaining.seconds%60)} giây)"
                else:
                    # Hết thời gian khóa
                    user["locked_until"] = None
                    user["failed_attempts"] = 0
                    self.save_users()
        return None
    
    def login(self):
        """Xử lý đăng nhập"""
        print("\n" + "="*50)
        print("ĐĂNG NHẬP HỆ THỐNG")
        print("="*50)
        
        email = input("📧 Email: ").strip().lower()
        password = input("🔒 Mật khẩu: ")
        
        # Kiểm tra khóa tài khoản
        lock_status = self.is_account_locked(email)
        if lock_status:
            print(f"\n⛔ {lock_status}")
            return False
        
        # Kiểm tra email tồn tại
        if email not in self.users:
            print("\n❌ Email không tồn tại trong hệ thống!")
            return False
        
        user = self.users[email]
        
        # Kiểm tra mật khẩu
        if user["password"] == password:
            # Đăng nhập thành công
            user["failed_attempts"] = 0
            user["locked_until"] = None
            user["last_login"] = datetime.now().isoformat()
            self.save_users()
            
            print(f"\n✅ ĐĂNG NHẬP THÀNH CÔNG!")
            print(f"   👤 Người dùng: {email}")
            print(f"   🎭 Vai trò: {user['role'].upper()}")
            print(f"   🕐 Thời gian: {datetime.now().strftime('%H:%M:%S %d/%m/%Y')}")
            
            # Mô phỏng chuyển hướng
            self.redirect_by_role(user["role"])
            return True
        else:
            # Đăng nhập thất bại
            user["failed_attempts"] += 1
            remaining_attempts = 5 - user["failed_attempts"]
            
            print(f"\n❌ SAI MẬT KHẨU!")
            print(f"   ⚠️ Lần thử sai thứ: {user['failed_attempts']}/5")
            
            if remaining_attempts > 0:
                print(f"   💡 Bạn còn {remaining_attempts} lần thử")
            else:
                # Khóa tài khoản 5 phút
                lock_time = datetime.now() + timedelta(minutes=5)
                user["locked_until"] = lock_time.isoformat()
                print(f"\n⛔ TÀI KHOẢN ĐÃ BỊ KHÓA!")
                print(f"   🔐 Tài khoản sẽ mở khóa lúc: {lock_time.strftime('%H:%M:%S')}")
            
            self.save_users()
            return False
    
    def redirect_by_role(self, role):
        """Mô phỏng chuyển hướng theo vai trò"""
        print("\n" + "="*50)
        print("CHUYỂN HƯỚNG ĐẾN TRANG CHỦ...")
        print("="*50)
        
        if role == "admin":
            print("🎯 Trang quản trị viên:")
            print("   • Quản lý người dùng")
            print("   • Xem báo cáo hệ thống")
            print("   • Cài đặt hệ thống")
        elif role == "user":
            print("👤 Trang người dùng:")
            print("   • Thông tin cá nhân")
            print("   • Lịch sử hoạt động")
            print("   • Cài đặt tài khoản")
        else:
            print("👥 Trang khách")
        
        print("\n✓ Chuyển hướng thành công!")
    
    def show_login_attempts(self):
        """Hiển thị lịch sử đăng nhập (demo)"""
        print("\n📊 LỊCH SỬ ĐĂNG NHẬP (DEMO):")
        print("-"*40)
        
        for email, data in self.users.items():
            # Kiểm tra trạng thái
            if data["failed_attempts"] >= 5 and data["locked_until"]:
                try:
                    lock_time = datetime.fromisoformat(data["locked_until"].replace('Z', '+00:00'))
                    if datetime.now() < lock_time:
                        status = "⛔ Tạm khóa"
                    else:
                        status = "✅ Hoạt động"
                except:
                    status = "❓ Không xác định"
            else:
                status = "✅ Hoạt động"
            
            # Định dạng thời gian đăng nhập cuối
            last_login = data.get("last_login")
            formatted_last_login = self.format_last_login(last_login)
            
            print(f"📧 {email}")
            print(f"   Vai trò: {data['role']}")
            print(f"   Trạng thái: {status}")
            print(f"   Lần đăng nhập cuối: {formatted_last_login}")
            print(f"   Số lần thử sai gần nhất: {data['failed_attempts']}")
            print()
    
    def run(self):
        """Chạy hệ thống"""
        while True:
            print("\n" + "="*50)
            print("HỆ THỐNG QUẢN LÝ ĐĂNG NHẬP")
            print("="*50)
            print("1. Đăng nhập")
            print("2. Xem trạng thái đăng nhập (demo)")
            print("3. Thoát")
            print("="*50)
            
            choice = input("👉 Lựa chọn của bạn (1-3): ").strip()
            
            if choice == "1":
                self.login()
            elif choice == "2":
                self.show_login_attempts()
            elif choice == "3":
                print("\n👋 Cảm ơn bạn đã sử dụng hệ thống! Tạm biệt!")
                break
            else:
                print("\n⚠️ Lựa chọn không hợp lệ! Vui lòng chọn 1-3.")

if __name__ == "__main__":
    system = LoginSystem()
    system.run()