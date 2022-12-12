# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# # b) Подумайте как наделить бота ""интеллектом""

import random


def AI_bot(N, a) -> int:
    # Функцианал бота
    if N % 2 == 1:
        take_candy_bot = (28 - a) + 1
    else:
        take_candy_bot = random.randint(1, 28)
    return take_candy_bot

def player() -> int:
    # Функцианал игрока
    make_candy = int(input('Берите конфеты от 1 до 28 '))
    return make_candy


def candy_game():
    # Количество конфет в партии
    N = 121
    print(f'Количество конфет в партии {N}')
    # Выберите режим игры
    print('Выберите режим игры\n'
          '1 - Режим игры с ботом\n'
          '2 - Режим игры с другом')
    game_mode = int(input("Вибирите число 1 или 2: "))
    if game_mode == 1:
        player1 = input("Введите имя 1 игрока: ")
        player2 = 'Bot'
    else:
        player1 = input("Введите имя 1 игрока: ")
        player2 = input("Введите имя 2 игрока: ")

    # Жеребьевка
    def lottery() -> tuple:
        number_player1 = random.randint(1, 6)
        number_player2 = random.randint(1, 6)
        print(f'Бросок кубика игрока {player1}={number_player1}')
        print(f'Бросок кубика игрока {player2}={number_player2}')
        if number_player1 > number_player2:
            print(f'Первым ходит игрок {player1}')
            return player1, player2
        elif number_player1 < number_player2:
            print(f'Первым ходит игрок {player2}')
            return player2, player1
        else:
            print("Ничья. Бросаем кубики снова")
            return lottery()

    # Игра
    def game(N: int):

        players = lottery()
        a = 1
        if 'Bot' in players:
            while N > 0:
                if players[0] == 'Bot':
                    print(f'Ходит игрок {players[0]}')
                    N -= AI_bot(N, a)
                    print(f'На столе осталось конфет {N}')
                    if N <= 0:
                        print(f'Игрок {players[0]} победил!')
                        break
                    print(f'Ходит игрок {players[1]}')
                    a = player()
                    N -= a
                    print(f'На столе осталось конфет {N}')
                    if N <= 0:
                        print(f'Игрок {players[1]} победил!')
                        break
                else:
                    print(f'Ходит игрок {players[1]}')
                    a = player()
                    N -= a
                    print(f'На столе осталось конфет {N}')
                    if N <= 0:
                        print(f'Игрок {players[1]} победил!')
                        break
                    print(f'Ходит игрок {players[0]}')
                    N -= AI_bot(N, a)
                    print(f'На столе осталось конфет {N}')
                    if N <= 0:
                        print(f'Игрок {players[0]} победил!')
                        break
        else:
            while N > 0:
                print(f'Ходит игрок {players[0]}')
                N -= player()
                print(f'На столе осталось конфет {N}')
                if N <= 0:
                    print(f'Игрок {players[0]} победил!')
                    break
                print(f'Ходит игрок {players[1]}')
                N -= player()
                print(f'На столе осталось конфет {N}')
                if N <= 0:
                    print(f'Игрок {players[1]} победил!')
                    break

    game(N)


candy_game()
