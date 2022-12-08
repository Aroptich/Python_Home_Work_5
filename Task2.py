# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# # b) Подумайте как наделить бота ""интеллектом""

import random


def candy_game():
    # Количество конфет в партии
    N = 121
    print(f'Количество конфет в партии {N}')

    player1 = input("Введите имя 1 игрока: ")
    player2 = input("Введите имя 2 игрока: ")

    # Жеребьевка
    def lottery() -> tuple[str]:
        while True:
            number_player1 = random.randint(1, 6)
            number_player2 = random.randint(1, 6)
            print(f'Бросок кубика игрока {player1}={number_player1}')
            print(f'Бросок кубика игрока {player2}={number_player2}')
            if number_player1 > number_player2:
                print(f'Первым ходит игрок {player1}')
                return player1, player2
                break
            elif number_player1 < number_player2:
                print(f'Первым ходит игрок {player2}')
                return player2, player1
                break
            else:
                print("Ничья. Бросаем кубики снова")

    # Игра
    def game(N: int):
        if status == True:
            players = lottery()
            while N > 0:
                print(f'Ходит игрок {players[0]}')
                take_candy = int(input('Берите конфеты от 1 до 28 '))
                N -= take_candy
                print(f'На столе осталось конфет {N}')
                if N <= 0:
                    print(f'Игрок {players[0]} победил!')
                    status = False
                print(f'Ходит игрок {players[1]}')
                take_candy = int(input('Берите конфеты от 1 до 28 '))
                N -= take_candy
                print(f'На столе осталось конфет {N}')
                if N <= 0:
                    print(f'Игрок {players[1]} победил!')
                    status = False

    game(N)
    exit()


candy_game()
