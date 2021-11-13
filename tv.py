# Задача: Создать программу, имитирующую телевизор как объект.
#         Должна быть возможность вводить номер канала,
#         а также увеличивать и уменьшать громкость.
#

class Tv:
    def __init__(self, channel=0, volume=0):
        self.channel = channel
        self.volume = volume

    def channel_up(self, choice=1):
        self.channel += choice
        if self.channel < 0:
            self.channel = 0
        elif self.channel > 100:
            self.channel = 100

    def channel_down(self, choice=1):
        self.channel -= choice
        if self.channel < 0:
            self.channel = 0
        elif self.channel > 100:
            self.channel = 100

    def change_volume(self):
        self.volume += 1
        if self.volume < 0:
            self.volume = 0
        elif self.volume > 100:
            self.volume = 0

    def __str__(self):
        print("Канал: ", self.channel)
        print("Уровень громкости: ", self.volume)


def main():
    tv = Tv()
    tv.__str__()
    choice = None
    while choice != "0":
        print(
            """
            Меню:
            0 - выйти
            1 - управлять канналами
            2 - управлять звуком
            """
        )
        choice = input("Ваш выбор: ")
        print()
        if choice == '1':
            print(
                """
            Меню канналов:
            "+" - плюс один канал
            "-" - минус один канал
            "или" введите номер канала            
            """)
            choice_channel = input("Ваш выбор: ")
            if choice_channel == '+':
                tv.channel_up()
                tv.__str__()
            elif choice_channel == '-':
                tv.channel_down()
                tv.__str__()
            elif choice_channel.isdigit():
                tv.channel_up(int(choice_channel))
                tv.__str__()
            else:
                print("Ошибка: номер канала должно быть целое число")


main()
