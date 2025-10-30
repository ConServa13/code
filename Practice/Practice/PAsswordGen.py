import random
import string

def password_gen(a):
    simvols = string.digits + string.ascii_letters + string.punctuation
    password = ''.join(random.choice(simvols) for i in range(a))
    return password
    #nums = string.digits
    #strr = string.ascii_letters
    #a = list(nums)
    #b = list(strr)
    #print(a)
    #print(b)
    #password = ''
print(password_gen(18)," << Это лучший вариант!!!")
print(password_gen(16))
print(password_gen(12))
print(password_gen(10))