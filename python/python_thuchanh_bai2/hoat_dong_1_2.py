# HOẠT ĐỘNG 1:
# Bài tập 1.1

ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))

print("Ho ten:", ho_ten)
print("Nam sinh:", nam_sinh)
print("Diem trung binh:", diem_tb)

# Bài tập 1.2

print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
print("Dong 1", end=" | ")
print("Dong 2")

# Bài tập 1.3
# Cách 1: 
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")
# Cách 2: 
print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(
    ho_ten, nam_sinh, diem_tb))
# Cách 3:
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" %
      (ho_ten, nam_sinh, diem_tb))

# HOẠT ĐỘNG 2: 
# Bài tập 2.1
"""
Chu thich nhieu dong:
Chuong trinh quan ly diem sinh vien - Buoi 2
"""

ho_ten = "Tran Thi B"  
# Bài tập 2.2 

s1 = "Xin chao"
s2 = "Ban co khoe khong?"
s3 = """Day la
mot chuoi
nhieu dong"""

s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", ban ten gi?"

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)