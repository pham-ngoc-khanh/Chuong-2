# Bài 1: Tạo class học viên

class HocVien:
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    # b) Hiển thị thông tin
    def show_info(self):
        print("===== THÔNG TIN HỌC VIÊN =====")
        print("Họ tên:", self.ho_ten)
        print("Ngày sinh:", self.ngay_sinh)
        print("Email:", self.email)
        print("Điện thoại:", self.dien_thoai)
        print("Địa chỉ:", self.dia_chi)
        print("Lớp:", self.lop)

    # c) Thay đổi thông tin (có giá trị mặc định)
    def change_info(self, dia_chi="Phú Thọ", lop="IT14.2"):
        self.dia_chi = dia_chi
        self.lop = lop
        print("\n>>> Đã cập nhật thông tin!")

# d) Chương trình chính
if __name__ == "__main__":
    # Tạo đối tượng
    hv1 = HocVien(
        "Phạm Ngọc Khánh",
        "24/09/2005",
        "phamk8607@gmail.com",
        "0949207116",
        "Phú Thọ",
        "CNTT"
    )

    # Hiển thị ban đầu
    hv1.show_info()

    # Thay đổi thông tin
    hv1.change_info()

    # Hiển thị sau khi thay đổi
    hv1.show_info()