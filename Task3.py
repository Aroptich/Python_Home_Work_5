import turtle
import random


def rules_of_the_game(winning_positions):
# Проверка игроков на выйграш
    examination =[i for i in winning_positions.values()]
    print(examination[0:10:4])
    if sum(examination[0:3]) == 3:
        print('win player 1')
    elif sum(examination[0:3]) == -3:
        print('win player 2')
    elif sum(examination[3:7]) == 3:
        print('win player 1')
    elif sum(examination[3:7]) == -3:
        print('win player 2')
    elif sum(examination[7:10]) == 3:
        print('win player 1')
    elif sum(examination[7:10]) == -3:
        print('win player 2')
    elif sum(examination[0:10:4]) == 3:
        print('win player 1')
    elif sum(examination[0:10:4]) == -3:
        print('win player 2')
    elif sum(examination[1:7:3]) == 3:
        print('win player 1')
    elif sum(examination[1:7:3]) == -3:
        print('win player 2')
    elif sum(examination[2:8:3]) == 3:
        print('win player 1')
    elif sum(examination[2:8:3]) == -3:
        print('win player 2')
    elif sum(examination[3:9:3]) == 3:
        print('win player 1')
    elif sum(examination[3:9:3]) == -3:
        print('win player 2')
    elif sum(examination[3:7:2]) == 3:
        print('win player 1')
    elif sum(examination[3:7:2]) == -3:
        print('win player 2')
    else:
        print('Ничья')


def drawing_rectangle():
    #Рисование квадратов для построения поля
    turtle.ht()
    turtle.speed(10)
    turtle.pendown()
    turtle.width(5)
    turtle.color('black')
    for step in range(4):
        turtle.forward(100)
        turtle.left(90)


def drawing_cross(coordinats_point):
    #Рисование крестиков
    x, y = coordinats_point
    turtle.goto(x, y)
    turtle.pendown()
    turtle.width(3)
    turtle.color('red')
    turtle.speed(20)

    for i in range(1, 5):
        turtle.right(45)
        turtle.forward((50 ** 2 + 50 ** 2) ** 0.5 - 8)
        turtle.right(180)
        turtle.forward((50 ** 2 + 50 ** 2) ** 0.5 - 8)
        turtle.right(45)
    turtle.penup()


def drawing_zeros(coordinats_point):
    #Рисование ноликов
    x, y = coordinats_point
    turtle.goto(x, y)
    turtle.penup()
    turtle.forward(42)
    turtle.left(90)
    turtle.pendown()
    turtle.speed(2000)
    turtle.pendown()
    turtle.width(3)
    turtle.color('green')
    for i in range(361):
        turtle.left(1)
        turtle.forward(0.75)
    turtle.penup()


def drawing_field():
    #Рисование игрового поля
    for i in range(3):
        for step in range(3):
            drawing_rectangle()
            turtle.goto(100 + (100 * step), 0 - (100 * i))
        turtle.penup()
        turtle.goto(0, -100 - (100 * i))
    turtle.penup()



def lottery() -> tuple[str]:
    # Розыгрыш первого хода
    player1 = input("Введите имя 1 игрока: ")
    player2 = input("Введите имя 2 игрока: ")
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

drawing_field()
def game():
    # Игровой процесс
    # Словарь с координатами ячеек
    cell_coordinates = {1: (50, 50),
                        2: (150, 50),
                        3: (250, 50),
                        4: (50, -50),
                        5: (150, -50),
                        6: (250, -50),
                        7: (50, -150),
                        8: (150, -150),
                        9: (250, -150)}
    empty_dictionary = {k: 0 for k in range(1, 10)}
    players = lottery()
    try:

        list_a = [filter(lambda x: x == 0, [i for i in empty_dictionary.values()])]
        list_b = [filter(lambda x: x == 1, [i for i in empty_dictionary.values()])]
        if len(list_a) > len(list_b):
            for step in range(9 // 2 + 1):
                make_a_move = int(input(f'{players[1]} Выберите клетку: '))
                if empty_dictionary[make_a_move] == 0 and empty_dictionary[make_a_move] != 'x':
                    drawing_zeros(cell_coordinates[make_a_move])
                    empty_dictionary[make_a_move] = 'o'
                    print(empty_dictionary)
                make_a_move = int(input(f' {players[0]} Выберите клетку: '))
                if empty_dictionary[make_a_move] == 0 and empty_dictionary[make_a_move] != 'o':
                    drawing_cross(cell_coordinates[make_a_move])
                    empty_dictionary[make_a_move] = 'x'
                    print(empty_dictionary)

        else:
            for step in range(9 // 2 + 1):
                make_a_move = int(input(f'{players[0]} Выберите клетку: '))
                if empty_dictionary[make_a_move] == 0 and empty_dictionary[make_a_move] != 'o':
                    drawing_cross(cell_coordinates[make_a_move])
                    empty_dictionary[make_a_move] = 'x'
                    print(empty_dictionary)
                make_a_move = int(input(f'{players[1]} Выберите клетку: '))
                if empty_dictionary[make_a_move] == 0 and empty_dictionary[make_a_move] != 'x':
                    drawing_zeros(cell_coordinates[make_a_move])
                    empty_dictionary[make_a_move] = 'o'
                    print(empty_dictionary)



        return empty_dictionary
    except KeyError:
        return game()


game()
