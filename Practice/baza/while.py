a = ["стоп", "stop", "Stop", "Стоп"]
b = True
while b:
    if input("Введите: ") == a[0] or a[1] or a[2] or a[3]:
        b = False
    else:
        b = True 
    
