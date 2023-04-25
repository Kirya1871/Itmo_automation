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

