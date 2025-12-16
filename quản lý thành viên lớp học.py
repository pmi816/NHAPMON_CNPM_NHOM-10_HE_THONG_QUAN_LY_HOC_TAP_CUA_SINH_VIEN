class SinhVien:
    def __init__(self, ma_sv, ho_ten, email):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.email = email
    def hien_thi(self):
        print("Mã SV:", self.ma_sv)
        print("Họ tên:", self.ho_ten)
        print("Email:", self.email)
class LopHoc:
    def __init__(self, ten_lop, giang_vien):
        self.ten_lop = ten_lop
        self.giang_vien = giang_vien
        self.ds_sinh_vien = []
    def hien_thi_ds(self):
        if len(self.ds_sinh_vien) == 0:
            print("Lớp chưa có sinh viên.")
            return
        print(f"Danh sách sinh viên lớp {self.ten_lop}:")
        for sv in self.ds_sinh_vien:
            print(f"- {sv.ma_sv} | {sv.ho_ten}")
    def tim_sv(self, ma_sv):
        for sv in self.ds_sinh_vien:
            if sv.ma_sv == ma_sv:
                sv.hien_thi()
                return
        print("Không tìm thấy sinh viên.")
    def them_sv(self, sv, nguoi_dung):
        if nguoi_dung != self.giang_vien:
            print("❌ Không có quyền thêm sinh viên.")
            return

        self.ds_sinh_vien.append(sv)
        print("✅ Thêm sinh viên thành công.")
    def xoa_sv(self, ma_sv, nguoi_dung):
        if nguoi_dung != self.giang_vien:
            print("❌ Không có quyền xóa sinh viên.")
            return

        for sv in self.ds_sinh_vien:
            if sv.ma_sv == ma_sv:
                self.ds_sinh_vien.remove(sv)
                print("✅ Đã xóa sinh viên.")
                return

        print("Không tìm thấy sinh viên.")