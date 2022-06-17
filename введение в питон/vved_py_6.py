secret_word = input("Введите слово для игры: ")
print("\033[2J")

win = False
letters = []

player_one = input("Первый игрок, введи свое имя: ")
player_two = input("Второй игрок, введи свое имя: ")
player_three = input("Третий игрок, введи свое имя: ")

counts = [0, 0, 0]
player_moves = 1
player = player_one

while win == False:
    word = ""
    if player_moves == 1:
        player = player_one
    elif player_moves == 2:
        player = player_two
    else:
        player = player_three
    
    print(player, "ваш ход! Крутите барабан и называйте букву!")
    answer = input("введите букву: ")

    while len(answer) > 1:
        print("нужно ввести одну букву")
        answer = input("Введите букву: ")

    if answer in secret_word and answer not in letters:
        print("Вы угадали букву:", answer)
        counts[player_moves-1] += 1
        print(player, "вас счет:", counts[player_moves-1])
    elif answer in letters:
        print("Вы уже использовали эту букву")
    else:
        print("буква", answer, "отсутствует в слове")
        player_moves += 1
        if player_moves > 3:
            player_moves = 1

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
        print("---", player_one, "ваш счет:", counts[0], "\n---", player_two, "ваш счет:", counts[1], "\n---", player_three, "ваш счет:", counts[2])
        
