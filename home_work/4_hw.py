class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def Plowad(self):
        Plowad = self.length * self.width
        return Plowad
    def Perimetr(self):
        Perimetr = 2 * (self.length + self.width)
        return Perimetr

figura = Rectangle(5, 7)
figura1 = Rectangle(7, 9)
figura2 = Rectangle(3, 4)

object = figura.Plowad()
object1 = figura1.Plowad()
object2 = figura2.Plowad()
perimetr = figura.Perimetr()
perimetr1 = figura1.Perimetr()
perimetr2= figura2.Perimetr()
print(f"Прямоугольник 1: Площадь = {object}, Периметр = {perimetr}")
print(f"Прямоугольник 2: Площадь = {object1}, Периметр = {perimetr1}")
print(f"Прямоугольник 3: Площадь = {object2}, Периметр = {perimetr2}")


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self, a, b):
        result = a + b
        print(result)

    def multiplication(self, a, b):
        result = a * b
        print(result)

    def division(self, a, b):
        result = a / b
        print(result)

    def subtraction(self, a, b):
        result = a - b
        print(result)

math_obj = Math(7, 9)
math_obj.addition(10, 20)
math_obj.multiplication(10, 20)
math_obj.division(10, 2)
math_obj.subtraction(10, 5)

