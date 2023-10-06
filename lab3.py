# Функція для зчитування тексту з файлу
def read_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Помилка при зчитуванні з файлу: {str(e)}")
        return None


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

text = "308714515213312402905710418555501115402504306308115402503905666595439904115308107307120618904213904403604439123904115595428213123819914699213123513666608820115114501126908888515115601115308123405213501439444501126104115595312512555515115503403123614402428904126308702119601618403710115114120405439513219604213555618714904416595"

# Ініціалізуємо словник для збереження чисел та їх частоти
number_frequency = {}

# Розбиваємо стрічку на числа по трійках і підраховуємо частоту кожного числа
for i in range(0, len(text), 3):
    number = text[i:i + 3]
    if number in number_frequency:
        number_frequency[number] += 1
    else:
        number_frequency[number] = 1

# Виводимо результати
for number, frequency in number_frequency.items():
    print(f'Число "{number}": {frequency} разів')


