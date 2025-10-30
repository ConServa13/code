fl = open("1.txt", "r", encoding="utf-8")
f2 = fl.readlines()
w1 = {}
for i in f2:
    if i.strip():
        names, age = i.strip().split(", ")
        w1[names] = int(age)

w2 = {}
w3 = {}
for nam, ag in w1.items():
    if ag < 18:
        w2[nam] = int(ag)
    else:
        w3[nam] = int(ag)
fl.close()

fl2 = open("yes.txt", 'a',  encoding="utf-8")
def men18():
    fl2.write(str(w2) + '\n')
def bol18():
    fl2.write(str(w3) + '\n')
a = input('больше или меньше 18? Ответ напишите в формате ">" или "<" ')
if a == '<':
    men18()
if a == '>':
    bol18()
#if a != '<' or '>':
    #print('нет такокого действия!')

fl2.close()
