class Vector:
    def __init__(self, x, y, z):
        self.__x, self.__y, self.__z = x, y, z

    def sum (self, vect2):
        return Vector(self.__x + vect2.__x, self.__y + vect2.__y, self.__z + vect2.__z)

    def dot_product(self, vect2):
        return self.__x * vect2.__x + self.__y * vect2.__y + self.__z * vect2.__z

    def multiply (self, skalar):
        return Vector(self.__x * skalar, self.__y * skalar, self.__z * skalar)

    def substraction (self, vect2):
        return Vector(self.__x - vect2.__x, self.__y - vect2.__y, self.__z - vect2.__z)

    def GetVector(self):
        print('Координаты результирующего вектора равны: (', self.__x, ',' , self.__y, ',' , self.__z, ')' , sep='')


def main():
    vect1 = Vector(int(input('Введите координаты первого вектора: \nx = ')), int(input('y = ')), int(input('z = ')))

    answer = int(input(('Выберите необходимую операцию: \n1 - сложение,\n2 - скалярное произведение,\n3 - умножение на скаляр,\n4 - вычитание\n')))

    if answer == 3:
        vect2 = vect1.multiply(int(input("Введите скаляр: ")))
        vect2.GetVector()

    elif (answer == 1 or answer == 2 or answer == 4):
        vect2 = Vector(int(input('Введите координаты второго вектора: \nx = ')), int(input('y = ')), int(input('z = ')))

        if answer == 1:
            vect3 = vect1.sum(vect2)
            vect3.GetVector()

        elif answer == 2:
            dot_product_result = vect1.dot_product(vect2)
            print("Результат скалярного произведения: ", dot_product_result)

        else:
            vect3 = vect1.substraction(vect2)
            vect3.GetVector()

    else:
        print("BAAAD INPUT")

if __name__ == '__main__':
    main()
