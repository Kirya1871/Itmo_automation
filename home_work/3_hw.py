
def f4(a, b ,c):
    if a > 10 and b > 10 and c > 10:
        print('yes')
    else:
        print('no')

def f3(a):
    if a == 12 or a == 1 or a == 2:
        print('зима')
    elif a == 3 or a == 4 or a == 5:
        print('весна')
    elif a == 6 or a == 7 or a == 8:
        print('лето')
    elif a == 9 or a == 10 or a == 11:
        print('осень')
    else:
        print('введите от 1 до 12')



def f2(a, b):
    if abs (a-b) == 135:
        print('yes')
    else:
        print('no')

def f1(a, b):
    print(max (a, b))



f1(1, 2)

f2(1.0, 136)

f3(5)
f4(11, 11, 112)
