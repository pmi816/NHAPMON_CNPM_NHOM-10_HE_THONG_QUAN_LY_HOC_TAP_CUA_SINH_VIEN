# ================================
# HỆ THỐNG NHẬN & XỬ LÝ THÔNG BÁO
# Đối tượng: Sinh viên
# ================================

notifications = [
    {
        "id": 1,
        "title": "Bài tập mới",
        "content": "Nộp bài Python trước thứ 6",
        "class": "CTK42",
        "read": False
    },
    {
        "id": 2,
        "title": "Điểm giữa kỳ",
        "content": "Điểm giữa kỳ đã được cập nhật",
        "class": "CTK42",
        "read": False
    },
    {
        "id": 3,
        "title": "Nghỉ học",
        "content": "Lớp CTK43 nghỉ học thứ 2",
        "class": "CTK43",
        "read": True
    }
]

# ======= CHỨC NĂNG =======

def xem_thong_bao_moi():
    print("\n--- THÔNG BÁO CHƯA ĐỌC ---")
    found = False
    for n in notifications:
        if not n["read"]:
            print(f'{n["id"]}. {n["title"]} ({n["class"]})')
            found = True
    if not found:
        print("Không có thông báo mới")

def danh_dau_da_doc():
    id_tb = int(input("Nhập ID thông báo cần đánh dấu đã đọc: "))
    for n in notifications:
        if n["id"] == id_tb:
            n["read"] = True
            print("✔ Đã đánh dấu thông báo là đã đọc")
            return
    print("❌ Không tìm thấy thông báo")

def loc_thong_bao_chua_doc():
    print("\n--- DANH SÁCH CHƯA ĐỌC ---")
    for n in notifications:
        if not n["read"]:
            print(f'{n["id"]}. {n["title"]} - {n["class"]}')

def xem_chi_tiet():
    id_tb = int(input("Nhập ID thông báo: "))
    for n in notifications:
        if n["id"] == id_tb:
            print("\n--- CHI TIẾT THÔNG BÁO ---")
            print("Tiêu đề:", n["title"])
            print("Nội dung:", n["content"])
            print("Lớp:", n["class"])
            print("Trạng thái:", "Đã đọc" if n["read"] else "Chưa đọc")
            return
    print("❌ Không tìm thấy thông báo")

def nhan_theo_lop():
    lop = input("Nhập tên lớp: ")
    print(f"\n--- THÔNG BÁO LỚP {lop} ---")
    found = False
    for n in notifications:
        if n["class"] == lop:
            print(f'{n["id"]}. {n["title"]}')
            found = True
    if not found:
        print("Không có thông báo cho lớp này")

# ======= MENU CHÍNH =======

def menu():
    while True:
        print("""
==============================
HỆ THỐNG THÔNG BÁO SINH VIÊN
1. Xem thông báo mới
2. Đánh dấu đã đọc
3. Lọc thông báo chưa đọc
4. Xem chi tiết thông báo
5. Nhận thông báo theo lớp
0. Thoát
==============================
""")
        choice = input("Chọn chức năng: ")

        if choice == "1":
            xem_thong_bao_moi()
        elif choice == "2":
            danh_dau_da_doc()
        elif choice == "3":
            loc_thong_bao_chua_doc()
        elif choice == "4":
            xem_chi_tiet()
        elif choice == "5":
            nhan_theo_lop()
        elif choice == "0":
            print("👋 Thoát chương trình")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")

# ======= CHẠY CHƯƠNG TRÌNH =======
menu()