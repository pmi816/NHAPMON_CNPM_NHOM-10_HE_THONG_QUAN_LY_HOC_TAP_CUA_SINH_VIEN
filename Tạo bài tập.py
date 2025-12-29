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
