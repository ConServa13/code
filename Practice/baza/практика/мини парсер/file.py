f = open("open.txt", "r", encoding="utf-8")
f2 = f.readlines()
print (f2)
s = 0
for i in f2:
    if i.startswith("192."):
        s += 1
f.close()
print ("бло замечено", s, "странных адресов")


