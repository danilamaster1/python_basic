"""2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного
кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;"""

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        return f'{(self._length * self._width * 25 * 5) / 1000} тонн'


r_1 = Road(28, 5155)
print(r_1.weight())
