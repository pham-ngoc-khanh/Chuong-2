# Module phanso.py: Chứa các hàm tính toán cơ bản như cộng, trừ, nhân, chia phân số.

def cong(ps1, ps2):
    # ps1, ps2 là tuple (tu_so, mau_so)
    tu = ps1[0] * ps2[1] + ps2[0] * ps1[1]
    mau = ps1[1] * ps2[1]
    return (tu, mau)

def tru(ps1, ps2):
    tu = ps1[0] * ps2[1] - ps2[0] * ps1[1]
    mau = ps1[1] * ps2[1]
    return (tu, mau)

def nhan(ps1, ps2):
    tu = ps1[0] * ps2[0]
    mau = ps1[1] * ps2[1]
    return (tu, mau)

def chia(ps1, ps2):
    if ps2[0] == 0:
        raise ValueError("Không thể chia cho phân số có tử số bằng 0")
    tu = ps1[0] * ps2[1]
    mau = ps1[1] * ps2[0]
    return (tu, mau)

def hien_thi(ps):
    return f"{ps[0]}/{ps[1]}"
