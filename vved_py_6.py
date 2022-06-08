secret_word = input("Введите слово для игры: ")
print("\033[2J")

win = False
letters = []

player_one = input("Первый игрок, введи свое имя: ")
player_two = input("Второй игрок, введи свое имя: ")
player_three = input("Третий игрок, введи свое имя: ")
players = [player_one, player_two, player_three]

count_one = 0
count_two = 0
count_three = 0
counts = [count_one, count_two, count_three]

player_moves = 0

while win == False:
    word = ""
    answer = input(f"\n{players[player_moves]}, введите букву: ")

    while len(answer) > 1:
        print("нужно ввести одну букву")
        answer = input("Введите букву: ")

    if answer in secret_word and answer not in letters:
        print("Вы угадали букву:", answer)
        counts[player_moves] += 1
        print(f"{players[player_moves]}, вас счет: {counts[player_moves]}")
    elif answer in letters:
        print("Вы уже использовали эту букву")
    else:
        print("буква", answer, "отсутствует в слове")
        player_moves += 1
        if player_moves > 2:
            player_moves = 0

    letters.append(answer)

    for letter in secret_word:
        if letter in letters:
            word += letter
        else:
            word += "*"

    print("__[",word,"]__")

    if word == secret_word:
        win = True
        print("Игра окончена!")
        print(f"""\
---{player_one}, ваш счет: {counts[0]}
---{player_two}, ваш счет: {counts[1]}
---{player_three}, ваш счет: {counts[2]}
    """)
        
