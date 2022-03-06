"""4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости."""

from random import choice


class Car:

    turns = ['направо', 'налево']

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала {self.speed}км/с')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self):
        print(f'Машина {self.name} повернула {choice(self.turns)}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Превышение {self.name}' if self.speed > 60 else super().show_speed())


class WorkCar(Car):
    def show_speed(self):
        print(f'Превышение {self.name}' if self.speed > 40 else super().show_speed())


class PoliceCar(Car):
    pass


town = TownCar(69, 'green', 'volvo')
town.go()
town.stop()
town.turn()
town.turn()
town.show_speed()

work = WorkCar(39, 'red', 'Mazda')
work.go()
work.turn()
work.show_speed()

police = PoliceCar(100, 'black', 'lada', True)
print(police.is_police)
print(police.name)
print(police.color)
print(police.speed)
police.show_speed()
police.turn()
