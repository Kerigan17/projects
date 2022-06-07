from random import randint

count = 0
items = ["камень", "ножницы", "бумага"]
move = 10

for move in range(10):
    player = int(input("Сделайте ход - 1-камень, 2-ножницы, 3-бумага: "))

    while player > 3 or player <1:
        print("неверный ход")
        player = int(input("Сделайте ход - 1-камень, 2-ножницы, 3-бумага: "))

    comp = randint(1,3)

    print("Ваш ход -", items[player-1])
    print("Ход компьютера -", items[comp-1])

    if (player == 1 and comp == 2) or (player == 2 and comp == 3) or (player == 3 and comp == 1):
        count += 1
    elif player == comp:
        print("Ничья!")

    print("Вы победили:", count)

    if count == 3:
        break