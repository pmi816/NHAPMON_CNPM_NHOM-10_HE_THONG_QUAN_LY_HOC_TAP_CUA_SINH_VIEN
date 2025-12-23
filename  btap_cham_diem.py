
# ====== LỚP BÀI TẬP ======
class Assignment:
    def __init__(self, aid, title, description):
        self.aid = aid
        self.title = title
        self.description = description

    def __str__(self):
        return f"[{self.aid}] {self.title} - {self.description}"


# ====== LỚP BÀI NỘP ======
class Submission:
    def __init__(self, aid, student_name, content):
        self.aid = aid
        self.student_name = student_name
        self.content = content
        self.score = None
        self.feedback = None


# ====== DỮ LIỆU ======
assignments = []
submissions = []


# ====== MENU GIẢNG VIÊN ======
def lecturer_menu():
    while True:
        print("\n--- GIẢNG VIÊN ---")
        print("1. Tạo bài tập")
        print("2. Chấm bài & cho điểm")
        print("3. Gửi nhận xét")
        print("0. Quay lại")

        choice = input("Chọn: ")

        # Tạo bài tập
        if choice == "1":
            aid = input("Mã bài tập: ")
            title = input("Tiêu đề: ")
            desc = input("Mô tả: ")
            assignments.append(Assignment(aid, title, desc))
            print(" Đã tạo bài tập")

        # Chấm điểm
        elif choice == "2":
            for sub in submissions:
                if sub.score is None:
                    print(f"\nSinh viên: {sub.student_name}")
                    print(f"Bài tập: {sub.aid}")
                    print(f"Nội dung: {sub.content}")
                    sub.score = float(input("Nhập điểm: "))
            print(" Đã chấm điểm")

        # Gửi nhận xét
        elif choice == "3":
            for sub in submissions:
                if sub.feedback is None:
                    sub.feedback = input(
                        f"Nhận xét cho {sub.student_name} (bài {sub.aid}): "
                    )
            print(" Đã gửi nhận xét")

        elif choice == "0":
            break
        else:
            print(" Sai lựa chọn")


# ====== MENU SINH VIÊN ======
def student_menu():
    name = input("Nhập tên sinh viên: ")

    while True:
        print("\n--- SINH VIÊN ---")
        print("1. Xem chi tiết bài tập")
        print("2. Nộp bài")
        print("3. Xem điểm & phản hồi")
        print("0. Quay lại")

        choice = input("Chọn: ")

        # Xem bài tập
        if choice == "1":
            if not assignments:
                print(" Chưa có bài tập")
            for a in assignments:
                print(a)

        # Nộp bài
        elif choice == "2":
            aid = input("Nhập mã bài tập: ")
            content = input("Nội dung bài làm: ")
            submissions.app1end(Submission(aid, name, content))
            print(" Nộp bài thành công")

        # Xem điểm
        elif choice == "3":
            found = False
            for sub in submissions:
                if sub.student_name == name:
                    found = True
                    print(f"\nBài: {sub.aid}")
                    print(f"Điểm: {sub.score}")
                    print(f"Nhận xét: {sub.feedback}")
            if not found:
                print(" Chưa có bài nộp")

        elif choice == "0":
            break
        else:
            print(" Sai lựa chọn")


# ====== CHƯƠNG TRÌNH CHÍNH ======
def main():
    while True:
        print("\n=== BÀI TẬP & CHẤM ĐIỂM ===")
        print("1. Giảng viên")
        print("2. Sinh viên")
        print("0. Thoát")

        role = input("Chọn vai trò: ")

        if role == "1":
            lecturer_menu()
        elif role == "2":
            student_menu()
        elif role == "0":
            print(" Kết thúc chương trình")
            break
        else:
            print(" Sai lựa chọn")


main()