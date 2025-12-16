# ====== LỚP TÀI LIỆU ======
class Document:
    def __init__(self, doc_id, name, file_type, permission="all"):
        self.doc_id = doc_id
        self.name = name
        self.file_type = file_type
        self.permission = permission  # all / lecturer
        self.deleted = False

    def __str__(self):
        return f"[{self.doc_id}] {self.name}.{self.file_type} (Quyền: {self.permission})"


# ====== DỮ LIỆU ======
documents = []
ALLOWED_TYPES = ["pdf", "docx", "pptx", "txt"]


# ====== MENU GIẢNG VIÊN ======
def lecturer_menu():
    while True:
        print("\n--- GIẢNG VIÊN: QUẢN LÝ TÀI LIỆU ---")
        print("1. Tải lên tài liệu")
        print("2. Kiểm soát quyền truy cập")
        print("3. Xóa tài liệu")
        print("0. Quay lại")

        choice = input("Chọn: ")

        # Tải tài liệu
        if choice == "1":
            doc_id = input("Mã tài liệu: ")
            name = input("Tên tài liệu: ")
            file_type = input("Loại file (pdf/docx/pptx/txt): ")

            if file_type not in ALLOWED_TYPES:
                print(" File không hợp lệ")
                continue

            documents.append(Document(doc_id, name, file_type))
            print(" Tải tài liệu thành công")

        # Kiểm soát quyền
        elif choice == "2":
            doc_id = input("Nhập mã tài liệu: ")
            for d in documents:
                if d.doc_id == doc_id and not d.deleted:
                    d.permission = input("Quyền (all/lecturer): ")
                    print(" Đã cập nhật quyền")
                    break
            else:
                print(" Tài liệu không tồn tại")

        # Xóa tài liệu
        elif choice == "3":
            doc_id = input("Nhập mã tài liệu cần xóa: ")
            for d in documents:
                if d.doc_id == doc_id:
                    d.deleted = True
                    print(" Đã xóa tài liệu")
                    break
            else:
                print(" Không tìm thấy tài liệu")

        elif choice == "0":
            break
        else:
            print(" Sai lựa chọn")


# ====== MENU SINH VIÊN ======
def student_menu():
    while True:
        print("\n--- SINH VIÊN: TÀI LIỆU HỌC TẬP ---")
        print("1. Xem danh sách tài liệu")
        print("2. Xem tài liệu trực tuyến")
        print("3. Tải tài liệu xuống")
        print("0. Quay lại")

        choice = input("Chọn: ")

        # Danh sách tài liệu
        if choice == "1":
            found = False
            for d in documents:
                if not d.deleted and d.permission == "all":
                    print(d)
                    found = True
            if not found:
                print(" Không có tài liệu")

        # Xem trực tuyến
        elif choice == "2":
            doc_id = input("Nhập mã tài liệu: ")
            for d in documents:
                if d.doc_id == doc_id and not d.deleted and d.permission == "all":
                    print(f" Đang xem: {d.name}.{d.file_type}")
                    break
            else:
                print(" Lỗi: File không tồn tại hoặc đã bị xóa")

        # Tải xuống
        elif choice == "3":
            doc_id = input("Nhập mã tài liệu: ")
            for d in documents:
                if d.doc_id == doc_id and not d.deleted and d.permission == "all":
                    print(f"⬇ Đã tải: {d.name}.{d.file_type}")
                    break
            else:
                print(" Lỗi khi tải: File hỏng hoặc không tồn tại")

        elif choice == "0":
            break
        else:
            print(" Sai lựa chọn")


# ====== CHƯƠNG TRÌNH CHÍNH ======
def main():
    while True:
        print("\n=== QUẢN LÝ TÀI LIỆU HỌC TẬP ===")
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
