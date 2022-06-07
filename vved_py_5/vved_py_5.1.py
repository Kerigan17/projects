from random import randint

count = 0

for move in range(10):
    player = int(input("Сделайте ход - 1-камень, 2-ножницы, 3-бумага: "))
    comp = randint(1,3)

    if player == 1:
        print("Ваш ход - камень")
    elif player == 2:
        print("Ваш ход - ножницы")
    elif player == 3:
        print("Ваш ход - бумага")

    if comp == 1:
        print("Ход компьютера - камень")
    elif comp == 2:
        print("Ход компьютера - ножницы")
    elif comp == 3:
        print("Ход компьютера - бумага")

    if (player == 1 and comp == 2) or (player == 2 and comp == 3) or (player == 3 and comp == 1):
        count += 1

    if player == comp:
        print("Ничья!")

    print("Вы победили:", count)

    if count == 3:
        break