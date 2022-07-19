lang = ""
result = ""
cipher = []
ALPHABET = ""
ALPHABET_RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET_EN = "abcdefghijklmnopqrstuvwxyz"

while lang != "EN" and lang != "RU":
    lang = input("Выберите язык - RU/EN: ")
    if lang == "RU":
        ALPHABET = ALPHABET_RU
    elif lang == "EN":
        ALPHABET = ALPHABET_EN
    else:
        print("\nК сожалению такого языка нет.")

message = input("\nВведите ваше сообщение: ").lower()
step = int(input("Введите шаг сдвига: "))

for symbol in message:
    new_ind = ALPHABET.find(symbol) + step
    cipher.append(new_ind)

for num in cipher:
    result += ALPHABET[num-step] 
