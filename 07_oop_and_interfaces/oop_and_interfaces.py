"""
OOP and interfaces.
"""

# Пункт 3.1. Сделайте в своём коде три примера наглядных методов-фабрик.
# Пример 1 (на основе кода Динамического массива из ASD1).

# Исходный код
import ctypes
class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        # С массивом будет работа в рамках исходной ёмкости,
        #  поэтому блок проверки закомментирован
        # if self.count == self.capacity:
        #    self.resize(2*self.capacity)
        for pos in range(self.count, i, -1):
            self.array[pos] = self.array[pos-1]
        self.array[i] = itm
        self.count += 1

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    # прочие методы класса DynArray опущены

# Измененный вариант кода:
# осталась возможность задать массив с длиной по умолчанию,
# добавлена возможность задать массив с заданной длиной.
import ctypes
class DynArray:

    __secret_key = 12345
    __default_capacity = 16
    
    def __init__(self, 
                 capacity = None,
                 array = None,
                 secret_key = None
                 ):
        if secret_key != DynArray.__secret_key:
            raise Exception("Calling the constructor method is prohibited")
        self.count = 0
        self.capacity = capacity
        self.array = array

    @staticmethod
    def with_specified_capacity(capacity):
        return DynArray(capacity=capacity,
                        array=(capacity * ctypes.py_object)(),
                        secret_key=DynArray.__secret_key
                       )

    @staticmethod
    def with_default_capacity():
        return DynArray(capacity=DynArray.__default_capacity,
                        array=(DynArray.__default_capacity * ctypes.py_object)(),
                        secret_key=DynArray.__secret_key
                       )

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        # С массивом будет работа в рамках исходной ёмкости,
        #  поэтому блок проверки закомментирован
        # if self.count == self.capacity:
        #    self.resize(2*self.capacity)
        for pos in range(self.count, i, -1):
            self.array[pos] = self.array[pos-1]
        self.array[i] = itm
        self.count += 1

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    # прочие методы класса DynArray опущены


# Пример 2 (придуманный пример: сумма двух чисел).
class SummaOfTwo:
    
    __secret_key = '12345'
    __default_summand = 0

    def __init__(self, 
                 summand_a=None, 
                 summand_b=None, 
                 summa_a_and_b=None, 
                 secret_key=None
                ):
        if secret_key != SummaOfTwo.__secret_key:
            raise Exception("Calling the constructor method is prohibited")
        self.summa_a_and_b = summa_a_and_b
        self.summand_a = summand_a
        self.summand_b = summand_b

    @staticmethod
    def of_two_summands(summand_a, summand_b):
        return SummaOfTwo(summand_a, 
                          summand_b,
                          summand_a + summand_b,
                          secret_key=SummaOfTwo.__secret_key
                         )

    @staticmethod
    def of_one_summand(summand_a):
        return SummaOfTwo(summand_a, 
                          SummaOfTwo.__default_summand,
                          summand_a + SummaOfTwo.__default_summand,
                          secret_key=SummaOfTwo.__secret_key
                         )

    @staticmethod
    def of_no_summands():
        return SummaOfTwo(SummaOfTwo.__default_summand, 
                          SummaOfTwo.__default_summand,
                          SummaOfTwo.__default_summand + SummaOfTwo.__default_summand,
                          secret_key=SummaOfTwo.__secret_key
                         )


# Пример 3 (придуманный пример: фигуры).
# Для каждой фигуры свой статический метод.
# Этот метод получает размеры фигуры,
# а конструктору метод выдаёт список координат точек
# (считая, что нижний левый угол имеет координаты (0,0),
#  а отрисовка идёт от него вправо, вверх, влево, вниз).
class Shapes:

    __secret_key = '12345'

    def __init__(self,
                 array_of_points = None,
                 secret_key = None
                ):
        if secret_key != Shapes.__secret_key:
            raise Exception("Calling the constructor method is prohibited")
        self.array_of_points = array_of_points

    @staticmethod
    def point_without_dimensions():
        return Shapes([(0,0)], 
                      secret_key=Shapes.__secret_key
                     )

    @staticmethod
    def length_of_line(length_dot):
        return Shapes([(0,0),
                       (length_dot,0)
                      ], 
                      secret_key=Shapes.__secret_key
                     )

    @staticmethod
    def legs_length_of_right_triangle(leg_a_dot, leg_b_dot):
        return Shapes([(0,0),
                       (leg_a_dot,0),
                       (0,leg_b_dot)
                      ], 
                      secret_key=Shapes.__secret_key
                     )

    @staticmethod
    def side_length_of_square(side_length_dot):
        return Shapes([(0,0),
                       (side_length_dot,0),
                       (side_length_dot,side_length_dot),
                       (0,side_length_dot)
                      ], 
                      secret_key=Shapes.__secret_key
                     )

    @staticmethod
    def sides_length_of_rectangle(side_length_a_dot, side_length_b_dot):
        return Shapes([(0,0),
                       (side_length_a_dot,0),
                       (side_length_a_dot,side_length_b_dot),
                       (0,side_length_b_dot)
                      ], 
                      secret_key=Shapes.__secret_key
                     )
        

# Пункт 3.2. Если вы когда-нибудь использовали интерфейсы или абстрактные классы, напишите несколько примеров их правильного именования.
# Интерфейсы и абстрактные классы не использовал. Взял пример из одной из статей про абстрактные классы. В этом примере 
# название абстрактного класса было Animal, а название класса-наследника Cat. Переименовал абстрактный класс.

from abc import ABC, abstractmethod

class AnimalFactory(ABC):
    @abstractmethod
    def get_name(self):
        return "animal"

class Cat(AnimalFactory):
    def get_name(self):
        return super().get_name() + " cat"
