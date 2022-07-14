from ast import While
import string, random

status = False
symbols = string.printable.replace(string.whitespace, "")

long_password = int(input("Какой длинны вы хотите пароль? "))
while status == False:
    if long_password >= 7 and long_password <= 20:
        password = ""
        for symbol in range(7):
            one_symbol = str(random.choice(symbols))
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
    else:
        while long_password < 7 or long_password > 20:
            print("Пароль должен быть больше 7 и меньше 20 символов.")
            long_password = int(input("Какой длинны вы хотите пароль? "))
        

