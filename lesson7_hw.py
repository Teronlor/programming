
# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — 
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


import random as rnd

class Matrix:
    def __init__(self, matrix):
        self.__matrix = matrix
        self.__row_num = len(matrix)
        self.__col_num = len(matrix[0])

    def __str__(self):
        res_str = ""
        for row in self.__matrix:
            res_str += " ".join([str(num) for num in row]) + "\n"
        return res_str

    def __add__(self, other):
        res_matrix = [[]]
        other_row_num = len(other.__matrix)
        other_col_num = len(other.__matrix[0])
        if self.__row_num == other_row_num and self.__col_num == other_col_num:
            res_matrix = [[self.__matrix[j][i] + other.__matrix[j][i] for i in range(self.__col_num)] for j in range(self.__row_num)]
        else:
            print("Operation is not possible for matrices of different sizes!")
        return Matrix(res_matrix)


# numRows = int(input("Input number of rows: "))
# numCols = int(input("Input number of columns: "))
numRows = 2
numCols = 3
list_of_lists = [[rnd.randint(0, 20) for _ in range(numCols)] for x in range(numRows)]
matr = Matrix(list_of_lists)
print(f'Initial matrix is: \n{matr}')
another_list_of_lists = [[rnd.randint(0, 20) for _ in range(numCols)] for x in range(numRows)]
another_matr = Matrix(another_list_of_lists)
print(f'Another matrix is: \n{another_matr}')
print(f'Result matrix: \n{matr + another_matr}')

#############


class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        self.matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                self.matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matr]))

     
        
my_matrix = Matrix([[9, 1, 10],
                    [2, 7, 55],
                    [76, 0, 1]],
                   [[43, 99, 33],
                    [1, 1, 2],
                    [4, 50, 300]])

print(my_matrix.__add__())





# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
# К типам одежды в этом проекте относятся пальто и костюм. 
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: 
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). 
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.



class Clothes():
    def get_tissue_consumption(self):
        pass

    @property
    def tissue_consumption(self):
        pass


class Suit(Clothes):
    def __init__(self, height):
        self.__height = height

    @property
    def height(self):
        return self.__height

    def get_tissue_consumption(self):
        return 2 * self.__height + 0.3

    @property
    def tissue_consumption(self):
        return self.get_tissue_consumption()


class Coat(Clothes):
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def get_tissue_consumption(self):
        return self.__size/6.5 + 0.5

    @property
    def tissue_consumption(self):
        return self.get_tissue_consumption()


size = int(input("Input int size for a coat: "))
coat = Coat(size)
print(f'Tissue consumption for the coat in size {coat.size}: {coat.tissue_consumption}')

height = float(input("Input height for a suit: "))
suit = Suit(height)
print(f'Tissue consumption for the suit with height {suit.height}: {suit.tissue_consumption}')



################




class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height
        
    def get_square_c(self):
        return self.size / 6.5 + 0.5   
    def get_square_j(self):
        return self.height * 2 + 0.
    
    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

        
class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_c = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'

           
class Jacket(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_j}'



coat_1 = Coat(50,1.8)
costume_1 = Jacket(48,1.78)


print(coat_1)
print(costume_1)
print(coat_1.get_sq_full)
print(costume_1.get_sq_full)
print(costume_1.get_square_c())
print(costume_1.get_square_j())






# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. 
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). 
# В классе должны быть реализованы методы перегрузки арифметических операторов: 
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, 
# умножение и обычное (не целочисленное) деление клеток, соответственно. 
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
#  иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. 
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. 
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. 
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. 
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.





class Cell:
    def __init__(self, count):
        self.__count = count

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        diff = self.count - other.count
        if diff > 0:
            return Cell(diff)
        else:
            print("Operation is impossible because difference is negative...")
            return None

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(int(self.count / other.count))

    def __str__(self):
        return f'{self.count} cells'

    def make_order(self, cells_in_row):
        full_rows = self.count // cells_in_row
        mod_row = self.count % cells_in_row
        str_full_rows = "\n".join(['*' * cells_in_row for _ in range(full_rows)])
        if mod_row != 0 and str_full_rows:
            str_full_rows += "\n"
        str_full_rows += '*' * mod_row
        return str_full_rows


cell1 = Cell(int(input("Input 1st count of cells: ")))
cell2 = Cell(int(input("Input 2st count of cells: ")))
cell3 = Cell(int(input("Input 3rd count of cells: ")))
cell4 = Cell(int(input("Input 4th count of cells: ")))

print(f'Cell 1 + Cell 2 = {cell1 + cell2}')
print(f'Cell 2 - Cell 3 = {cell2 - cell3}')
print(f'Cell 3 * Cell 4 = {cell3 * cell4}')
print(f'Cell 4 / Cell 1 = {cell4 / cell1}')

cells_in_row = int(input("Input cells in row: "))
print(f'Make order for Cell 1: \n{cell1.make_order(cells_in_row)}')
print(f'Make order for Cell 2: \n{cell2.make_order(cells_in_row)}')
print(f'Make order for Cell 3: \n{cell3.make_order(cells_in_row)}')
print(f'Make order for Cell 4: \n{cell4.make_order(cells_in_row)}')


################



class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)


    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):

        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')


    def __mul__(self, other):

        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):

        return Cell(round(self.quantity // other.quantity))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells1 = Cell(33)
cells2 = Cell(9)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2) 



