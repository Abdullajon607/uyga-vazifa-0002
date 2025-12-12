
# 1-$

with open("info.txt", "w", encoding="utf-8") as f:
    f.write("Salom, Dunyo!")

# 2-$

with open("info.txt", "r") as f:
    matn = f.read()
print(matn)

# 3-$

with open("info.txt", "a", encoding="utf-8") as f:
    f.write("\nBu matn append orqali qoshildi.")

# 4-$

ism = input("Ism kiriting: ")
with open("ism.txt", "w") as f:
    f.write(ism)

# 5-$
mevalar = ["olma", "anor", "gilos", "shaftoli", "nok"]
with open("mevalar.txt", "w") as f:
    for meva in mevalar:
        f.write(meva + "\n")
    
# 6-$

with open("mevalar.txt", "r") as f:
    natija = f.read().splitlines()
print(natija)

# 7-$

with open("manba.txt", "w") as f:
    f.write("Python dasturlash tili")

with open("manba.txt", "r") as f:
    matn = f.read()

with open("yangi.txt", "w") as f:
    f.write(matn)

# 8-$

with open("matn.txt", "w") as f:
    f.write("Python dasturlash tili")

with open("matn.txt", "r") as f:
    matn = f.read()
sozlar = matn.split()
soni = len(sozlar)
print(soni)

# 9-$

with open("text.txt", "w") as f:
    f.write("birinchi qator, \nikkinchi qator, \nuchunchi qator, \ntortinchi qator")
with open("text.txt", "r") as f:
    qatorlar = f.readlines()
for qator in qatorlar[1::2]:
    print(qator.split())

# 10-$

import os
if os.path.exists("temp.txt"):
    os.remove("temp.txt")
    print(f"{"temp.txt"} fayl ochirildi")
else:
    print(f"{"temp.txt"} fayl mavjud emas.")