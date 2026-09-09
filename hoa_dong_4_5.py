toa_do = (3, 5)

print(toa_do)
print(type(toa_do))
# toa_do[0] = 10
x, y = toa_do

print("x =", x, ", y =", y)

# Doi gia tri 2 bien bang unpacking
a, b = 10, 20

a, b = b, a

print("a =", a, ", b =", b)
def divmod_demo(a, b):
    thuong = a // b
    du = a % b

    return thuong, du


thuong, du = divmod_demo(17, 5)

print(f"(Thuong, du) = ({thuong}, {du})")
import math

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)

print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")
import math

cac_diem = [(0, 0), (3, 4), (6, 8)]

for i in range(len(cac_diem)):
    for j in range(i + 1, len(cac_diem)):
        
        x1, y1 = cac_diem[i]
        x2, y2 = cac_diem[j]

        khoang_cach = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        print(
            f"{cac_diem[i]} -> {cac_diem[j]}: "
            f"{round(khoang_cach, 2)}"
        )