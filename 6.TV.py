class TV:
    def __init__(self, min_channel=1, max_channel=99, min_volume=0, max_volume=20):
        self.min_channel = min_channel
        self.max_channel = max_channel
        self.min_volume = min_volume
        self.max_volume = max_volume
        self.channel = min_channel
        self.volume = 10

    def set_channel(self, channel):
        if self.min_channel <= channel <= self.max_channel:
            self.channel = channel
            print(f"Канал встановлено на {self.channel}")
        else:
            print(f"Номер каналу має бути від {self.min_channel} до {self.max_channel}")

    def volume_up(self):
        if self.volume < self.max_volume:
            self.volume += 1
            print(f"Гучність підвищена до {self.volume}")
        else:
            print("Максимальна гучність!")

    def volume_down(self):
        if self.volume > self.min_volume:
            self.volume -= 1
            print(f"Гучність зменшена до {self.volume}")
        else:
            print("Мінімальна гучність!")

    def status(self):
        print(f"Канал: {self.channel}, Гучність: {self.volume}")

def main():
    tv = TV()
    while True:
        print("""\nМеню:
1 - Встановити канал
2 - Збільшити гучність
3 - Зменшити гучність
4 - Статус телевізора
0 - Вихід""")
        choice = input("Ваш вибір: ")

        if choice == "1":
            try:
                channel = int(input("Введіть номер каналу: "))
                tv.set_channel(channel)
            except ValueError:
                print("Некоректний номер каналу!")
        elif choice == "2":
            tv.volume_up()
        elif choice == "3":
            tv.volume_down()
        elif choice == "4":
            tv.status()
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Некоректний вибір!")

if __name__ == "__main__":
    main()