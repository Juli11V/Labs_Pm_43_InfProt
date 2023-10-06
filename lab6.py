# Функція для зчитування тексту з файлу
def read_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Помилка при зчитуванні з файлу: {str(e)}")
        return None

# Зчитуємо зашифрований текст з файлу
CipherText = read_from_file("PlayfairCipher_text.txt")

# Українська абетка
list1 = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']

key = "код"

# Функція для конвертації рядка в нижній регістр
def toLowerCase(text):
    return text.lower()

# Функція для генерації ключової матриці 5x7
def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements:
        matrix.append(compElements[:7])
        compElements = compElements[7:]

    return matrix


# Функція для пошуку елемента у матриці
def search(mat, element):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == element:
                return i, j

# Функція для видалення всіх пробілів у рядку
def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText


# Функція для дешифрування за допомогою Playfair Cipher
def decryptByPlayfairCipher(cipherText, key):
    key = removeSpaces(toLowerCase(key))
    matrix = generateKeyTable(key, list1)

    # Доповнюємо текст, якщо він не парний
    if len(cipherText) % 2 != 0:
        cipherText += 'x'

    plainText = ''
    for i in range(0, len(cipherText), 2):
        char1 = cipherText[i]
        char2 = cipherText[i + 1]
        row1, col1 = search(matrix, char1)
        row2, col2 = search(matrix, char2)

        if row1 is not None and row2 is not None:
            if row1 == row2:
                decrypted_char1, decrypted_char2 = decrypt_RowRule(matrix, row1, col1, row2, col2)
            elif col1 == col2:
                decrypted_char1, decrypted_char2 = decrypt_ColumnRule(matrix, row1, col1, row2, col2)
            else:
                decrypted_char1, decrypted_char2 = decrypt_RectangleRule(matrix, row1, col1, row2, col2)

            plainText += decrypted_char1 + decrypted_char2

    return plainText

# Функція для дешифрування за правилом рядка
def decrypt_RowRule(matrix, row1, col1, row2, col2):
    decrypted_char1 = matrix[row1][col1 - 1] if col1 > 0 else matrix[row1][-1]
    decrypted_char2 = matrix[row2][col2 - 1] if col2 > 0 else matrix[row2][-1]
    return decrypted_char1, decrypted_char2

# Функція для дешифрування за правилом стовпця
def decrypt_ColumnRule(matrix, row1, col1, row2, col2):
    decrypted_char1 = matrix[row1 - 1][col1] if row1 > 0 else matrix[-1][col1]
    decrypted_char2 = matrix[row2 - 1][col2] if row2 > 0 else matrix[-1][col2]
    return decrypted_char1, decrypted_char2

# Функція для дешифрування за правилом прямокутника
def decrypt_RectangleRule(matrix, row1, col1, row2, col2):
    decrypted_char1 = matrix[row1][col2]
    decrypted_char2 = matrix[row2][col1]
    return decrypted_char1, decrypted_char2

print("Зашифрований текст із лабораторної 5:", CipherText)
print("Ключовий текст:", key)

decryptedText = decryptByPlayfairCipher(CipherText, key)
print("Розшифрований текст:", decryptedText)
