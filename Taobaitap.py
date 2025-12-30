# ====== LỚP BÀI TẬP ======
class Assignment:
    def __init__(self, aid, title, content, subject, deadline, attachment):
        self.aid = aid
        self.title = title
        self.content = content
        self.subject = subject
        self.deadline = deadline
        self.attachment = attachment

    def __str__(self):
        return (
            f"\nMã bài tập: {self.aid}"
            f"\nTiêu đề: {self.title}"
            f"\nMôn học: {self.subject}"
            f"\nHạn nộp: {self.deadline}"
            f"\nFile đính kèm: {self.attachment}"
            f"\nNội dung: {self.content}"
        )


# ====== DỮ LIỆU ======
assignments = []
notifications = []
temp_assignment = None 
#thiết lập thông báo tự động 
def auto_notification(assignment):
    message = (
        f"Bài tập mới [{assignment.aid}] môn {assignment.subject} "
        f"đã được đăng. Hạn nộp: {assignment.deadline}"
    )
    notifications.append(message)

# ====== MENU GIẢNG VIÊN ======
def lecturer_menu():
    while True:
        print("\n--- GIẢNG VIÊN: TẠO BÀI TẬP ---")
        print("1. Nhập nội dung bài tập")
        print("2. đặt hạn nộp")
        print("3. gán môn học")
        print("4. lưu bài tập")
        print("0. Quay lại")

        choice = input("Chọn: ")

        # Khởi tạo biến tạm
        global temp_assignment

        # 1. Nhập nội dung bài tập
        if choice == "1":
            aid = input("Mã bài tập: ")
            title = input("Tiêu đề bài tập: ")
            content = input("Nội dung bài tập: ")
            temp_assignment = {
                "aid": aid,
                "title": title,
                "content": content,
                "subject": None,
                "deadline": None,
                "attachment": None
            }
            print("✅ Đã nhập nội dung bài tập")
        # 2. Đặt hạn nộp
        elif choice == "2":
            if not temp_assignment:
                print("❌ Chưa nhập nội dung bài tập")
            else:
                temp_assignment["deadline"] = input("Hạn nộp (dd/mm/yyyy): ")
                print("✅ Đã đặt hạn nộp")
    # 3. Gán môn học
        elif choice == "3":
            if not temp_assignment:
                print("❌ Chưa nhập nội dung bài tập")
            else:
                temp_assignment["subject"] = input("Tên môn học: ")
                print("✅ Đã gán môn học")
    # Lưu bài tập + TẠO THÔNG BÁO TỰ ĐỘNG
        elif choice == "4":
            if temp_assignment is None:
                print("❌ Chưa có bài tập để lưu")
            else:
                assignment = Assignment(
                    temp_assignment["aid"],
                    temp_assignment["content"],
                    temp_assignment["subject"],
                    temp_assignment["deadline"]
                )
                assignments.append(assignment)

                # 🔔 THIẾT LẬP THÔNG BÁO TỰ ĐỘNG
                auto_notification(assignment)

                temp_assignment = None
                print(" Đã lưu bài tập và gửi thông báo tự động")

        elif choice == "0":
            break
        else:
            print("❌ Sai lựa chọn")
            # ====== MENU SINH VIÊN ======
def student_menu():
    while True:
        print("\n--- SINH VIÊN ---")
        print("1. Xem bài tập")
        print("2. Xem thông báo")
        print("0. Quay lại")

        choice = input("Chọn: ")

        # ====== HIỂN THỊ BÀI TẬP CHO SINH VIÊN ======
        if choice == "1":
            if not assignments:
                print("❌ Chưa có bài tập")
            else:
                print("\n===== DANH SÁCH BÀI TẬP =====")
                for a in assignments:
                    print(a.display_for_student())
                    print("-" * 30)
 # ====== SINH VIÊN XEM THÔNG BÁO TỰ ĐỘNG ======
        elif choice == "2":
            if not notifications:
                print("❌ Không có thông báo")
            else:
                print("\n🔔 THÔNG BÁO")
                for n in notifications:
                    print("-", n)

        elif choice == "0":
            break
        else:
            print("❌ Sai lựa chọn")

# ====== CHƯƠNG TRÌNH CHÍNH ======
def main():
    while True:
        print("\n=== US-2.0: TẠO BÀI TẬP ===")
        print("1. Giảng viên")
        print("2. Sinh viên")
        print("0. Thoát")

        role = input("Chọn vai trò: ")

        if role == "1":
            lecturer_menu()
        elif role == "2":
            student_menu()
        elif role == "0":
            print("👋 Kết thúc chương trình")
            break
        else:
            print("❌ Sai lựa chọn")


main()
