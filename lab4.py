# -*- coding: utf-8 -*-

# Визначення алфавіту (українська абетка, обидва регістри)
alphabet = "абвгдеєжзиіїйклмнопрстуфхцчшщьюяАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
N = len(alphabet)

# Визначення номерів літер
letter_to_number = {letter: index for index, letter in enumerate(alphabet)}

# Парольна фраза (ключ)
password = "джаваскрипт"

# Формування гами
gamma = [letter_to_number[letter] for letter in password]

# Відкритий текст
plaintext = "КафедраПрикладноїМатематикиНаціональногоУніверситетуЛьвівськаПолітехнікаВжеБагатоРоківЗберігаєІПримножуєБагатіНауковіЙОсвітніТрадиціїНевтомноГотуєНовіПоколінняКваліфікованихКадрівУГалузяхПрикладноїМатематикиТаІнформатикиЗбагачуючиЇхІнтелектуальноІДуховно"

# Перетворення в нижній регістр і видалення розділових знаків і пробілів
plaintext = "".join(filter(lambda char: char in alphabet, plaintext))

# Шифрування
ciphertext = []
for i, plain_char in enumerate(plaintext):
    gamma_char = gamma[i % len(gamma)]  # "продовження" гами
    encrypted_char_index = (letter_to_number[plain_char] + gamma_char) % N
    encrypted_char = alphabet[encrypted_char_index]
    ciphertext.append(encrypted_char)

# Запис криптограми у файл
with open("encrypted.txt", "w", encoding="utf-8") as file:
    file.write("".join(ciphertext))

print("Зашифрований текст:", "".join(ciphertext))

# Розшифрування
decrypted_text = []
for i, encrypted_char in enumerate(ciphertext):
    gamma_char = gamma[i % len(gamma)]  # "продовження" гами
    decrypted_char_index = (letter_to_number[encrypted_char] - gamma_char + N) % N
    decrypted_char = alphabet[decrypted_char_index]
    decrypted_text.append(decrypted_char)

print("Розшифрований текст:", "".join(decrypted_text))
