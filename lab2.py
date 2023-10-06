import random

# Функція для запису тексту у файл
def write_to_file(filename, text):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Текст був записаний у файл '{filename}'.")
    except Exception as e:
        print(f"Помилка при записі у файл: {str(e)}")

# Функція для зчитування тексту з файлу
def read_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Помилка при зчитуванні з файлу: {str(e)}")
        return None

# Функція для шифрування тексту
def substitution_encrypt(plaintext, substitution_table):
    encrypted_text = ''
    for char in plaintext:
        if char in substitution_table:
            choices = substitution_table[char]
            encrypted_char = choices[random.randint(0, len(choices) - 1)]
            encrypted_text += encrypted_char
        elif char == ' ':
            encrypted_text += ' '  # Залиште пробіл без змін.
    return encrypted_text

ukrainian_substitution_table = {
    'А': ['512', '307', '418', '126', '439', '203', '914'],
    'Б': ['820'],
    'В': ['725', '609', '417', '308', '513'],
    'Г': ['104'],
    'Д': ['604'],
    'Е': ['702', '306'],
    'Є': ['817'],
    'Ж': ['219'],
    'З': ['405'],
    'И': ['213'],
    'І': ['115'],
    'Ї': ['323'],
    'Й': ['114'],
    'К': ['710', '428', '513'],
    'Л': ['819', '515'],
    'М': ['501'],
    'Н': ['312', '107', '699', '413'],
    'О': ['403', '608', '714'],
    'П': ['618'],
    'Р': ['904'],
    'С': ['402', '601', '318'],
    'Т': ['503', '201'],
    'У': ['416', '609'],
    'Ф': ['219'],
    'Х': ['908'],
    'Ц': ['504'],
    'Ч': ['595'],
    'Ш': ['512'],
    'Щ': ['312'],
    'Ь': ['814', '905'],
    'Ю': ['508'],
    'Я': ['614'],
    '_': ['417', '725', '213', '810', '306', '115'],
    ' ': ['999', '888', '777', '666', '555', '444', '119', '120', '121', '122', '123', '124']
}

# Згенеруйте відкритий текст
open_text = "Волинська місцевість чарівна природа річки лани в обіймах лісів Зима магічна літо яскраве спокій завжди поруч"
open_text = open_text.upper()

# Зашифруйте відкритий текст
encrypted_text = substitution_encrypt(open_text, ukrainian_substitution_table)

# Запишіть відкритий текст у файл
write_to_file("open_text.txt", open_text)

# Запишіть зашифрований текст у файл
write_to_file("encrypted_text.txt", encrypted_text)

print(f"Відкритий текст: {open_text}")
print(f"Зашифрований текст: {encrypted_text}")

# Функція для розшифрування тексту, виділяючи по 3 символи і шукаючи їх розшифрування в таблиці
def decryption_with_table(encrypted_text, substitution_table):
    decrypted_text = ''
    i = 0
    while i < len(encrypted_text):
        if encrypted_text[i:i+3] == '   ':  # Якщо зустріли три пробіли, то додаємо пробіл в розшифрований текст
            decrypted_text += ' '
            i += 3
        else:
            found = False
            for key, values in substitution_table.items():
                if encrypted_text[i:i+3] in values:
                    decrypted_text += key
                    found = True
                    i += 3
                    break
            if not found:
                # Якщо не знайдено відповідності, додаємо пустий символ
                decrypted_text += '_'
                i += 3
    return decrypted_text

# Зчитуємо зашифрований текст з файлу
encrypted_text = read_from_file("encrypted_text.txt")

# Розшифровуємо зашифрований текст
decrypted_text = decryption_with_table(encrypted_text, ukrainian_substitution_table)

print(f"Зашифрований текст: {encrypted_text}")
print(f"Розшифрований текст: {decrypted_text}")