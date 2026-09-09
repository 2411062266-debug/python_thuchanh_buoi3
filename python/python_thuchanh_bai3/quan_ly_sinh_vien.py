danh_sach_sv = [
    (8.5, "An"),
    (7.0, "Binh"),
    (9.2, "Chi"),
    (6.5, "Dung")
]

# Them sinh vien
danh_sach_sv.append((8.0, "Em"))

# Xoa mot sinh vien
danh_sach_sv.remove((7.0, "Binh"))

# Sua diem cho sinh vien o vi tri 0
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

# Kiem tra sinh vien co trong danh sach hay khong
print(
    "Co trong danh sach khong?",
    (9.2, "Chi") in danh_sach_sv
)

# Sap xep theo diem tang dan
danh_sach_sv.sort()

print("Danh sach khi sap xep theo diem tang dan:")

for diem, ten in danh_sach_sv:
    print(f"{ten}: {diem}")

# Sap xep giam dan
danh_sach_sv.sort(reverse=True)

print("Danh sach khi sap xep diem giam dan:")

for diem, ten in danh_sach_sv:
    print(f"{ten}: {diem}")