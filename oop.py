import math

# Пример абстракции и инкапсуляции: Класс Figure - абстрактный класс, который определяет интерфейс для всех фигур. Классы Round и Rectangle наследуют от Figure и реализуют метод square() для вычисления площади.
class Figure:
    def square(self) -> float:
        raise Exception('Use child class')
    


class Round(Figure):
    def __init__(self, radius: float):
        self.radius = radius
    def square(self) -> float:
        return math.pi * self.radius ** 2
    
# Полиморфизм: Метод square() в классе Round и Rectangle реализован по-разному, но мы можем использовать их одинаково, вызывая метод square() для объектов обоих классов.
class  Rectangle(Figure):
    def __init__(self, a, b):
        self.width = a
        self.height = b

    def square(self) -> float:
        return self.a * self.b
    
# наследование
class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


class FiguresList:
    def __init__(self, figures: list[Figure]):
        self.figures: list[Figure] = []
        for f in figures:
            if f["type"] == "round":
                self.figures.append(Round(f["params"][0]))
            elif f["type"] == "rectangle":
                self.figures.append(Rectangle(*f["params"]))
            elif f["type"] == "square":
                self.figures.append(Square(f["a"]))
            raise Exception("Unknown figure type")
        def square(self):
            return sum(f.square() for f in self.figures)