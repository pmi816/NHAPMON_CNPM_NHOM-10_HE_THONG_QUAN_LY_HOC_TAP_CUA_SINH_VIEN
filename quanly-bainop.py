import os
from datetime import datetime

# Hệ thống bắt đầu với dữ liệu trống
# Cấu trúc: { "TenBaiTap": { "HanNop": datetime, "DanhSachNop": { "MSSV": datetime } } }
du_lieu_he_thong = {}

def xoa_man_hinh():
    os.system('cls' if os.name == 'nt' else 'clear')

# Chức năng bổ trợ để tạo dữ liệu ban đầu
def tao_bai_tap():
    ten_bt = input("Nhập tên bài tập mới: ")
    han_str = input("Nhập hạn nộp (DD/MM/YYYY HH:MM): ")
    try:
        han_nop = datetime.strptime(han_str, "%d/%m/%Y %H:%M")
        du_lieu_he_thong[ten_bt] = {"HanNop": han_nop, "DanhSachNop": {}}
        print(f"✅ Đã tạo bài tập: {ten_bt}")
    except:
        print("❌ Sai định dạng thời gian!")

def nop_bai_gia_lap():
    ten_bt = input("Nộp cho bài tập nào: ")
    if ten_bt not in du_lieu_he_thong:
        print("❌ Không tìm thấy bài tập."); return
    
    mssv = input("Nhập MSSV nộp bài: ").upper()
    # Cho phép người dùng tự nhập thời gian nộp để kiểm tra đúng/trễ hạn
    tg_nop_str = input("Nhập thời gian nộp bài (DD/MM/YYYY HH:MM): ")
    try:
        tg_nop = datetime.strptime(tg_nop_str, "%d/%m/%Y %H:%M")
        du_lieu_he_thong[ten_bt]["DanhSachNop"][mssv] = tg_nop
        print(f"✅ Đã ghi nhận bài nộp của {mssv}")
    except:
        print("❌ Sai định dạng thời gian!")

# --- CÁC CHỨC NĂNG CHÍNH THEO YÊU CẦU (image_89b965.png) ---

def xem_danh_sach_bai_nop(ten_bt):
    nop = du_lieu_he_thong[ten_bt]["DanhSachNop"]
    print(f"\n--- 📋 DANH SÁCH BÀI NỘP: {ten_bt} ---")
    if not nop:
        print("Chưa có bài nộp nào.")
    else:
        for mssv in nop:
            print(f"- Bài nộp từ sinh viên: {mssv}")

def xem_ai_da_nop(ten_bt):
    nop = du_lieu_he_thong[ten_bt]["DanhSachNop"]
    print(f"\n--- 👥 SINH VIÊN ĐÃ NỘP BÀI ---")
    if not nop:
        print("Chưa có ai nộp bài.")
    else:
        print("Các MSSV đã nộp: ", ", ".join(nop.keys()))

def xem_ai_chua_nop(ten_bt):
    # Giả sử danh sách lớp cố định để đối chiếu
    danh_sach_lop = ["SV001", "SV002", "SV003", "SV004", "SV005"]
    nop = du_lieu_he_thong[ten_bt]["DanhSachNop"]
    chua_nop = [sv for sv in danh_sach_lop if sv not in nop]
    
    print(f"\n--- ❌ SINH VIÊN CHƯA NỘP BÀI ---")
    if not chua_nop:
        print("Tất cả sinh viên trong lớp đã nộp bài.")
    else:
        print("Các MSSV chưa nộp: ", ", ".join(chua_nop))

def xem_thoi_gian_nop(ten_bt):
    nop = du_lieu_he_thong[ten_bt]["DanhSachNop"]
    han_nop = du_lieu_he_thong[ten_bt]["HanNop"]
    
    print(f"\n--- ⏱ KIỂM TRA THỜI GIAN NỘP (Hạn: {han_nop}) ---")
    for mssv, tg in nop.items():
        trang_thai = "Đúng hạn" if tg <= han_nop else "⚠️ TRỄ HẠN"
        print(f"MSSV: {mssv} | Nộp lúc: {tg} | Trạng thái: {trang_thai}")

def xem_chi_tiet_bai_nop(ten_bt):
    mssv = input("\nNhập MSSV muốn xem chi tiết bài nộp: ").upper()
    nop = du_lieu_he_thong[ten_bt]["DanhSachNop"]
    if mssv in nop:
        print(f"📄 Chi tiết: Sinh viên {mssv} đã nộp bài thành công vào lúc {nop[mssv]}.")
    else:
        print("❌ Không tìm thấy dữ liệu bài nộp cho sinh viên này.")

def menu_quan_ly():
    ten_bt = input("Nhập tên bài tập muốn quản lý: ")
    if ten_bt not in du_lieu_he_thong:
        print("❌ Bài tập không tồn tại."); return
        
    while True:
        print(f"\n--- QUẢN LÝ BÀI NỘP [{ten_bt}] ---")
        print("1. Xem danh sách bài nộp")
        print("2. Xem sinh viên ai đã nộp bài")
        print("3. Xem ai chưa nộp bài")
        print("4. Xem thời gian nộp (Đúng hạn hay trễ hạn)")
        print("5. Xem chi tiết bài nộp")
        print("0. Quay lại")
        
        chon = input("Chọn chức năng (1-5): ")
        if chon == '1': xem_danh_sach_bai_nop(ten_bt)
        elif chon == '2': xem_ai_da_nop(ten_bt)
        elif chon == '3': xem_ai_chua_nop(ten_bt)
        elif chon == '4': xem_thoi_gian_nop(ten_bt)
        elif chon == '5': xem_chi_tiet_bai_nop(ten_bt)
        elif chon == '0': break

def main():
    while True:
        print("\n=== HỆ THỐNG KIỂM TRA BÀI NỘP ===")
        print("1. Tạo bài tập mới (Giảng viên)")
        print("2. Giả lập sinh viên nộp bài")
        print("3. Vào menu Quản lý bài nộp")
        print("0. Thoát")
        
        c = input("Lựa chọn: ")
        if c == '1': tao_bai_tap()
        elif c == '2': nop_bai_gia_lap()
        elif c == '3': menu_quan_ly()
        elif c == '0': break

if __name__ == "__main__":
    main()