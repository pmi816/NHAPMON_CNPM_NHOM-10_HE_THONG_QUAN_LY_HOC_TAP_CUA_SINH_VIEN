# teacher.py
# Chuc nang giang vien: cham diem va phan hoi

def xem_danh_sach_bai_nop(submissions):
    if not submissions:
        print("Chua co bai nop!")
        return
    for s in submissions:
        print(f"ID: {s.get('id')} | Diem: {s.get('score')} | Nhan xet: {s.get('comment')}")


def nhap_diem(submissions):
    id_sv = input("Nhap ID sinh vien: ")
    diem = input("Nhap diem: ")

    for s in submissions:
        if s.get("id") == id_sv:
            s["score"] = diem
            print("Da cap nhat diem!")
            return

    submissions.append({"id": id_sv, "score": diem})
    print("Da nhap diem moi!")


def nhap_nhan_xet(submissions):
    id_sv = input("Nhap ID sinh vien: ")
    nhan_xet = input("Nhap nhan xet: ")

    for s in submissions:
        if s.get("id") == id_sv:
            s["comment"] = nhan_xet
            print("Da luu nhan xet!")
            return

    submissions.append({"id": id_sv, "comment": nhan_xet})
    print("Da luu nhan xet moi!")


def luu_ket_qua():
    print("Da luu ket qua cham diem!")


def gui_phan_hoi(submissions):
    print("Dang gui phan hoi cho sinh vien...")
    for s in submissions:
        print(f"Gui ID {s.get('id')} | Diem: {s.get('score')} | Nhan xet: {s.get('comment')}")
