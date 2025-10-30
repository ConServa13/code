a = False
yes = 0
nums = "0123456789"
while a == False:
    b = input()
    c = len(b)
    if c < 8:
        print('eror1')
    else:
        yes += 1
    if b.isupper() or b.islower():
        print('eror2')
    else:
        yes += 1
    for i in b:
        if i in nums:
            yes += 1
        else:
            continue
            print('eror3', yes)
    if yes >= 3:
        print('OK!')
        a = True        
    else:
        print('eror4')
        yes = 0
        
        
