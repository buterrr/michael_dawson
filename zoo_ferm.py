# Моя зверюшка
# Виртуальный питомец, о котором пользователь может заботиться.
import random


class Critter(object):
    """ Виртуальный питомец """
    def __init__(self, name, hunger=0,
                 boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, ", и сейчас я чувствую себя", self.mood, "\n")
        self.__pass_time()

    def eat(self, food=4):
        food = int(input(f'Какое количество еды дать {self.name}? '))
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        fun = int(input(f'Сколько времени провести за игрой с {self.name}? '))
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def __str__(self):
        print("Имя - ", self.name)
        print("Голод - ", self.hunger)
        print("Скука - ", self.boredom)


def main():
    zoo = [Critter(input("Придумаейте имя для зверушки: "),
                   random.randint(0, 5), random.randint(0, 5)) for i in range(5)]
    choice = None
    while choice != "0":
        print(
            """
            Моя зверюшка
            0 - Выйти
            1 - Узнать о самочувствии зверюшки
            2 - Покормить зверюшку
            3 - Поиграть со зверюшкой
            """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("До свидания.")
        elif choice == "1":
            for i in zoo:
                i.talk()
        elif choice == "2":
            for i in zoo:
                i.eat()
        elif choice == "3":
            for i in zoo:
                i.play()
        elif choice == "info":
            for i in zoo:
                i.__str__()
        else:
            print("Извините, в меню нет пункта", choice)


main()
