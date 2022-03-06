"""1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) —
2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный)"""

from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            print(TrafficLight.__color[0])
            sleep(7)
            print(TrafficLight.__color[1])
            sleep(2)
            print(TrafficLight.__color[2])
            sleep(4)


traf_1 = TrafficLight()
traf_1.running()