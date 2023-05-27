def test_passing():
    assert (1, 2, 3) == (1, 2, 3)
def passing():
    print("hi")
passing()

def add (x, y):
    return x+y
print(add(1, 2))

def arg(a, b, c=2, d=3):
    return a+b+c+d
print(arg(1, 1))


def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d + ' '
print(range_arg('1', '6', '9', '4'))
print(range_arg('1', b='500', d='50', c='212'))
print(range_arg('a', 'b', 'c', 'd'))
