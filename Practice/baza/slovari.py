names = {'Maks': 97, 'Alex': 89, 'Masha': 100, "Vova": 63, "Gamer": 87, "Lena": 78, "Roma": 23}
best_names = {}
for i,e in names.items():
    if e > 80:
        best_names[i] = e
print (best_names)

best_name = ''
best_score = 0
#b = max(names.values())
for i,e in best_names.items():
    if e > best_score:
        best_name = i
        best_score = e

print(f"Максимальный балл {best_score} у студента {best_name}")