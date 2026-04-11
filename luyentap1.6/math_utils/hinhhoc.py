# Module hinhhoc.py: Chứa các hàm tính chu vi và diện tích của một số hình học đơn giản.
import math

# Hình tròn
def chu_vi_hinh_tron(r):
    return 2 * math.pi * r

def dien_tich_hinh_tron(r):
    return math.pi * r * r

# Hình chữ nhật
def chu_vi_hinh_chu_nhat(dai, rong):
    return 2 * (dai + rong)

def dien_tich_hinh_chu_nhat(dai, rong):
    return dai * rong
