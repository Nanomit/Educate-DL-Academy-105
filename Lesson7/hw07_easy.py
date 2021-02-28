import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

print("\nStart program 1")


class Triangle:
    def __init__(self, A, B, C):
        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        self.A = A
        self.B = B
        self.C = C
        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CA = sideLen(self.C, self.A)

    def areaTriangle(self):
        semi_perimeter = self.perimeterTriangle() / 2

        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.AB)
                         * (semi_perimeter - self.BC)
                         * (semi_perimeter - self.CA))

    def perimeterTriangle(self):
        return self.AB + self.BC + self.CA

    def heightTriangle(self):
        return self.areaTriangle() / (self.AB / 2)


result_triangle = Triangle((3, 3), (6, 8), (1, 10))

print('Площадь = {:.3f}'.format(result_triangle.areaTriangle()))
print('Высота = {:.3f}'.format(result_triangle.heightTriangle()))
print('Периметр = {:.3f}'.format(result_triangle.perimeterTriangle()))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

print("\nStart program 2")


class Trapeze:
    def __init__(self, A, B, C, D):

        def side_len(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        def area_triangle(len1, len2, len3):
            semi_perimeter = (len1 + len2 + len3) / 2

            return math.sqrt(semi_perimeter
                             * (semi_perimeter - len1)
                             * (semi_perimeter - len2)
                             * (semi_perimeter - len3))

        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.AB = side_len(self.A, self.B)
        self.BC = side_len(self.B, self.C)
        self.CD = side_len(self.C, self.D)
        self.DA = side_len(self.D, self.A)
        self.diagonal_AC = side_len(self.C, self.A)
        self.diagonal_BD = side_len(self.B, self.D)
        self.perimeter = self.AB + self.BC + self.CD + self.DA

        self.area = area_triangle(self.AB, self.diagonal_BD, self.DA) \
                    + area_triangle(self.diagonal_BD, self.BC, self.CD)

    def isTrapezeEqu(self):
        if self.diagonal_AC == self.diagonal_BD:
            return True
        return False


result_trapeze = Trapeze((3, 3), (6, 6), (12, 6), (15, 3))

print('Является данная фигура равнобедренной трапецией {}'.format(result_trapeze.isTrapezeEqu()))
print('Длинна стороны AB = {:.3f}'.format(result_trapeze.AB))
print('Длинна стороны BC = {:.3f}'.format(result_trapeze.BC))
print('Длинна стороны CD = {:.3f}'.format(result_trapeze.CD))
print('Длинна стороны DA = {:.3f}'.format(result_trapeze.DA))
print('Периметр = {:.3f}'.format(result_trapeze.perimeter))
print('Площадь = {:.3f}'.format(result_trapeze.area))
