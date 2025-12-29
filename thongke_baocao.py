# ==============================
# US-2.6 THONG KE & BAO CAO
# ==============================

import datetime

classes = set()
students = set()
subjects = set()
submitted_assignments = 0
report_history = []

# ----- NHAP DU LIEU -----
def nhap_lop_hoc():
    lop = input("Nhap ten lop hoc: ")
    classes.add(lop)

def nhap_sinh_vien():
    sv = input("Nhap ma sinh vien: ")
    students.add(sv)

def nhap_mon_hoc():
    mh = input("Nhap ten mon hoc: ")
    subjects.add(mh)

def nhap_bai_tap():
    global submitted_assignments
    trang_thai = input("Bai tap da nop? (y/n): ").lower()
    if trang_thai == "y":
        submitted_assignments += 1

# ----- THONG KE -----
def thong_ke_lop_hoc():
    return len(classes)

def thong_ke_sinh_vien():
    return len(students)

def thong_ke_mon_hoc():
    return len(subjects)

def thong_ke_bai_tap_da_nop():
    return submitted_assignments

# ----- BAO CAO -----
def xuat_bao_cao():
    report = {
        "Thoi gian": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "So lop hoc": thong_ke_lop_hoc(),
        "So sinh vien": thong_ke_sinh_vien(),
        "So mon hoc": thong_ke_mon_hoc(),
        "So bai tap da nop": thong_ke_bai_tap_da_nop()
    }

    print("\n===== BAO CAO TONG HOP =====")
    for k, v in report.items():
        print(f"{k}: {v}")

    report_history.append(report)
    print("Bao cao da duoc luu!")

def xem_lich_su_bao_cao():
    if not report_history:
        print("Chua co bao cao!")
        return

    print("\n===== LICH SU BAO CAO =====")
    for i, r in enumerate(report_history, start=1):
        print(f"\nBao cao {i}:")
        for k, v in r.items():
            print(f"{k}: {v}")

# ----- MENU -----
def menu():
    while True:
        print("""
--- US-2.6 THONG KE & BAO CAO ---
1. Nhap lop hoc
2. Nhap sinh vien
3. Nhap mon hoc
4. Nhap bai tap da nop
5. Xuat bao cao tong hop
6. Xem lich su bao cao
0. Thoat
""")
        chon = input("Chon chuc nang: ")

        if chon == "1":
            nhap_lop_hoc()
        elif chon == "2":
            nhap_sinh_vien()
        elif chon == "3":
            nhap_mon_hoc()
        elif chon == "4":
            nhap_bai_tap()
        elif chon == "5":
            xuat_bao_cao()
        elif chon == "6":
            xem_lich_su_bao_cao()
        elif chon == "0":
            break
        else:
            print("Lua chon khong hop le!")

menu()
