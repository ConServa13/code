from numpy.ma.core import append

fl = open("1.txt", "r", encoding="utf-8")
f2 = fl.readlines()
dan1 = []
for i in f2:
    i = i.strip()
    dan1.append(i)

dan2 = tuple(dan1)
#print (dan2)
for e in dan2:
    #print(e)
    w = e.split(",")
    #print(w)
    w2 = (dict.fromkeys(w))
    for w3 in w2:
        w4 = []
        print(w3)
        w4.append(w3)
        print(w4)
    #print (w2)
