# Tập tin Python main.py để sử dụng các hàm trong package math_utils
import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

from math_utils import phanso, hinhhoc

def main():
    # 1. Sử dụng module phanso
    ps1 = (1, 2) # 1/2
    ps2 = (1, 3) # 1/3
    
    print("--- Tính toán phân số ---")
    print(f"Cộng: {phanso.hien_thi(ps1)} + {phanso.hien_thi(ps2)} = {phanso.hien_thi(phanso.cong(ps1, ps2))}")
    print(f"Trừ: {phanso.hien_thi(ps1)} - {phanso.hien_thi(ps2)} = {phanso.hien_thi(phanso.tru(ps1, ps2))}")
    print(f"Nhân: {phanso.hien_thi(ps1)} * {phanso.hien_thi(ps2)} = {phanso.hien_thi(phanso.nhan(ps1, ps2))}")
    print(f"Chia: {phanso.hien_thi(ps1)} : {phanso.hien_thi(ps2)} = {phanso.hien_thi(phanso.chia(ps1, ps2))}")

    # 2. Sử dụng module hinhhoc
    r = 5
    dai = 10
    rong = 4
    
    print("\n--- Tính toán hình học ---")
    print(f"Hình tròn (r={r}):")
    print(f"  Chu vi: {hinhhoc.chu_vi_hinh_tron(r):.2f}")
    print(f"  Diện tích: {hinhhoc.dien_tich_hinh_tron(r):.2f}")
    
    print(f"Hình chữ nhật (dài={dai}, rộng={rong}):")
    print(f"  Chu vi: {hinhhoc.chu_vi_hinh_chu_nhat(dai, rong)}")
    print(f"  Diện tích: {hinhhoc.dien_tich_hinh_chu_nhat(dai, rong)}")

if __name__ == "__main__":
    main()
