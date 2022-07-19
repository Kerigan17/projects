from string import printable, whitespace
from random import choice

status = False
symbols = printable.replace(whitespace, "")


while status == False:
    long_password = int(input("Какой длинны вы хотите пароль? "))
    if long_password < 7:
        print("\nПароль слишком короткий. Введите его снова")
    elif long_password > 20:
        print("\nПароль слишком длинный. Сделай короче")
    else:
        status = True

status = False
while status == False:
    password = ""
    for symbol in range(long_password):
        one_symbol = str(choice(symbols))
        password += one_symbol

    print("Пароль:", password)
    answer = input("Понравился полученный пароль? ")

    if answer == "да":
        status = True
        print("\nОтлично! Ваш новый пароль:", password)
    elif answer == "нет":
        print("\nА если такой? ")
    else:
        break
        
        

