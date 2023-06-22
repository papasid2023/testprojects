from random import *

a = randint(1, 100)

print('Добро пожаловать в числовую угадайку')
print('Угадайте и введите число, которое загадал компьютер')

def is_valid(checktext):
    if checktext.isdigit() and 0 < int(checktext) < 101:
        return True
    else:
        return False
        


n = input()

while is_valid(n) == True:
        if int(n) == int(a):
            print('Вы угадали, поздравляем!')
            break     
        if int(n) > int(a):
            print('Ваше число больше загаданного, попробуйте еще разок')
            n = input()
        if int(n) < int(a):
            print('Ваше число меньше загаданного, попробуйте еще разок')
            n = input()