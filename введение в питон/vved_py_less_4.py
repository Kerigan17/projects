message = input("Введите сообщение: ")
long = len(message)
short = long//2
letter = message.find('и')

cipher_one = message.replace("и", "о").replace("т", "с")
cipher_two = message[::-1]
cipher_three = message[1::2] + message[0::2]
cipher_four = "\u001b[32m\u001b[48;5;75m" + message
cipher_five = message[-1] + message[1:long-1] + message[0]
cipher_six = message[short:] + message[:short]
cipher_seven = message[:letter] + message[letter+1:] + message[letter] + " " + str(letter)

decoding_one = cipher_one.replace("о", "и").replace("с", "т")
decoding_two = cipher_two[::-1]
decoding_three = ""
for letters in range(short):
    decoding_three += cipher_three[short + letters]
    decoding_three += cipher_three[letters]
decoding_four = "\u001b[0m" + cipher_four[len(cipher_four)-long::]
decoding_five = cipher_five[-1] + cipher_five[1:len(cipher_five)-1] + cipher_five[0]
decoding_six = cipher_six[short:] + cipher_six[:short]
decoding_seven = cipher_seven[:letter] + str(cipher_seven[long-1]) + cipher_seven[letter:long-1]

print("Шифр 1:", cipher_one)
print("Шифр 2:", cipher_two)
print("Шифр 3:", cipher_three)
print("Шифр 4: ", cipher_four, "\u001b[0m", sep="")
print("Шифр 5:", cipher_five)
print("Шифр 6:", cipher_six)
print("Шифр 7:", cipher_seven)

print("Расшифровка 1:", decoding_one)
print("Расшифровка 2:", decoding_two)
print("Расшифровка 3:", decoding_three)
print("Расшифровка 4:", decoding_four)
print("Расшифровка 5:", decoding_five)
print("Расшифровка 6:", decoding_six)
print("Расшифровка 7:", decoding_seven)
