import sys
import math

# Thiết lập encoding UTF-8 để hiển thị tiếng Việt có dấu trong console
# Nếu hệ thống không hỗ trợ reconfigure, ta dùng phương án dự phòng (không dấu)
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

# --- Bài 1 ---
# Viết chương trình python tính tổng của các phần tử trong một list sau: _list= [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("--- Bài 1 ---")
_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tong = sum(_list1)
print(f"Tổng của list {_list1} là: {tong}")

# --- Bài 1.1 ---
# Cho tuple: _tuple = ('a', 'b', 'd', 'e'). Hãy thêm phần tử 'c' vào vị trí số 2 
# của _tuple trên để tạo ra _new_tuple = ('a', 'b', 'c', 'd', 'e').
print("\n--- Bài 1.1 ---")
_tuple1 = ('a', 'b', 'd', 'e')
# Chuyển sang list để chèn phần tử, sau đó chuyển ngược lại thành tuple
_temp_list = list(_tuple1)
_temp_list.insert(2, 'c')
_new_tuple1 = tuple(_temp_list)
print(f"Tuple ban đầu: {_tuple1}")
print(f"Tuple mới sau khi chèn 'c' vào vị trí số 2: {_new_tuple1}")


# --- Bài 2 ---
# Viết chương trình python tính tích của các phần tử trong một list sau: _list= [1, 2, 3, 4, 5]
print("\n--- Bài 2 ---")
_list2 = [1, 2, 3, 4, 5]
# Sử dụng math.prod để tính tích một cách tối ưu nhất (Python 3.8+)
tich = math.prod(_list2)
print(f"Tích của list {_list2} là: {tich}")

# --- Bài 2.2 ---
# Loại bỏ các phần tử có giá trị giống nhau trong một tuple, để tạo 1 tuple mới.
# Ví dụ: nhập vào _tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab'), thì thu được _new_tuple = ('b', 'c', 'd').
# Gợi ý: dùng hàm count.
print("\n--- Bài 2.2 ---")
_tuple2 = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
# Chỉ giữ lại các phần tử xuất hiện đúng 1 lần (loại bỏ hoàn toàn những phần tử có trùng lặp)
_new_tuple2 = tuple(x for x in _tuple2 if _tuple2.count(x) == 1)
print(f"Tuple ban đầu: {_tuple2}")
print(f"Tuple mới sau khi loại bỏ tất cả các phần tử trùng lặp: {_new_tuple2}")


# --- Bài 3 ---
# Cho đầu vào là _list= [1, 2, 3, 4, 5, 6, 7, 8, 9]. 
# Viết chương trình python tạo 2 list mới từ list đó cho. 
# Trong đó 1 list chỉ bao gồm số chẵn (even), 1 list chỉ bao gồm số lẻ (odd).
print("\n--- Bài 3 ---")
_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Sử dụng list comprehension để tách chẵn lẻ
even_list = [x for x in _list3 if x % 2 == 0]
odd_list = [x for x in _list3 if x % 2 != 0]
print(f"List ban đầu: {_list3}")
print(f"List số chẵn (even): {even_list}")
print(f"List số lẻ (odd): {odd_list}")

# --- Bài 3.3 ---
# Loại bỏ trùng lặp trong một tuple, để tạo 1 tuple mới. 
# Ví dụ: nhập vào _tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab'), thì thu được _new_tuple = ('ab', 'b', 'e', 'c', 'd').
# Gợi ý: dùng hàm count.
print("\n--- Bài 3.3 ---")
_tuple3 = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
# dict.fromkeys() là cách hiệu quả nhất để loại bỏ trùng lặp mà vẫn giữ nguyên thứ tự
_new_tuple3 = tuple(dict.fromkeys(_tuple3))
print(f"Tuple ban đầu: {_tuple3}")
print(f"Tuple mới sau khi loại bỏ trùng lặp (giữ lại 1 phần tử): {_new_tuple3}")

# --- Bài 4 ---
# Cho danh sách ban đầu _list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']. 
# Tạo danh sách mới chứa 2 phần tử ở vị trí thứ 2 và thứ 3 _new = ['White', 'Black']
print("\n--- Bài 4 ---")
_list4 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
_new4 = _list4[2:4] # Lấy từ chỉ số 2 đến trước chỉ số 4
print(f"Danh sách ban đầu: {_list4}")
print(f"Danh sách mới (vị trí 2 và 3): {_new4}")

# --- Bài 5 ---
# Cho danh sách đầu vào _list = ['zero', 'three']. 
# Tạo ra danh sách mới _new = ['zero', 'one', 'two', 'three'] bằng cách thêm các phần tử vào danh sách ban đầu.
print("\n--- Bài 5 ---")
_list5 = ['zero', 'three']
_new5 = _list5.copy()
_new5.insert(1, 'one')
_new5.insert(2, 'two')
print(f"Danh sách ban đầu: {_list5}")
print(f"Danh sách sau khi thêm 'one', 'two': {_new5}")

# --- Bài 7 ---
# Viết chương trình tạo một list mới bằng cách:
print("\n--- Bài 7 ---")
_list7 = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
print(f"List đầu vào: {_list7}")

# 7.1: Loại bỏ tất cả các phần tử có giá trị giống nhau (không giữ lại phần tử nào nếu bị trùng)
_new7_1 = [x for x in _list7 if _list7.count(x) == 1]
print(f"7.1 - Loại bỏ tất cả phần tử trùng lặp: {_new7_1}")

# 7.2: Với các phần tử trùng lặp chỉ giữ lại 1 phần tử
_new7_2 = list(dict.fromkeys(_list7))
print(f"7.2 - Chỉ giữ lại 1 phần tử của các giá trị trùng: {_new7_2}")

# --- Bài 8 ---
# Viết chương trình lấy ra số lớn nhất trong list: _list= [11, 2, 23, 45, 6, 9].
print("\n--- Bài 8 ---")
_list8 = [11, 2, 23, 45, 6, 9]
print(f"Số lớn nhất trong {_list8} là: {max(_list8)}")

# --- Bài 9 ---
# Viết chương trình lấy ra số nhỏ nhất trong list: _list= [11, 2, 23, 45, 6, 9].
print("\n--- Bài 9 ---")
_list9 = [11, 2, 23, 45, 6, 9]
print(f"Số nhỏ nhất trong {_list9} là: {min(_list9)}")

# --- Bài 10 ---
# Viết chương trình copy một list cho trước thành một list mới.
print("\n--- Bài 10 ---")
_list10 = [1, 2, 3, 4, 5]
_new10 = _list10.copy()
print(f"List gốc: {_list10}")
print(f"List copy: {_new10}")

# --- Bài 11 ---
# Nhập vào từ bàn phím số n và list cho trước, tìm các từ có độ dài lớn hơn n từ list đó.
print("\n--- Bài 11 ---")
_list11 = ['apple', 'banana', 'orange', 'kiwi', 'plum']
# Để thuận tiện, ta giả định n = 5 (Bạn có thể dùng n = int(input("Nhập n: ")))
n = 5
print(f"List cho trước: {_list11}, n = {n}")
result11 = [word for word in _list11 if len(word) > n]
print(f"Các từ có độ dài lớn hơn {n}: {result11}")

# --- Bài 12 ---
# Đếm số chuỗi thỏa mãn điều kiện: độ dài >= giá trị đầu vào, ký tự đầu tiên và cuối cùng giống nhau.
print("\n--- Bài 12 ---")
_list12 = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
# Giả định độ dài đầu vào >= 4
n_len = 4
print(f"List đầu vào: {_list12}, độ dài >= {n_len}")
count12 = 0
for s in _list12:
    if len(s) >= n_len and len(s) > 0 and s[0] == s[-1]:
        count12 += 1
print(f"Số chuỗi thỏa mãn điều kiện: {count12}")
