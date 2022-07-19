message = input("Введите ваше сообщение: ").lower()
step = int(input("Введите шаг сдвига: "))

cipher = []
ALPHABET_RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
result = ""

for symbol in message:
    new_ind = ALPHABET_RU.find(symbol) + step
    cipher.append(new_ind)

for num in cipher:
    result += ALPHABET_RU[num-step] 

