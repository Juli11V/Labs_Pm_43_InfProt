# Функція для запису тексту у файл
def write_to_file(filename, text):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Текст був записаний у файл '{filename}'.")
    except Exception as e:
        print(f"Помилка при записі у файл: {str(e)}")

# Функція для конвертації рядка в нижній регістр
def toLowerCase(text):
    return text.lower()

# Функція для видалення всіх пробілів у рядку
def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText

# Функція для групування 2 елементів рядка як елемент списку
def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])
        group = i
    Diagraph.append(text[group:])
    return Diagraph

# Функція для заповнення літери у рядковому елементі,
# якщо 2 літери в одному рядку збігаються
def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    return new_word

# Українська абетка
list1 = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']

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

# Функція для виведення таблиці ключа в консоль
def printKeyTable(matrix):
    for row in matrix:
        print(" ".join(row))

# Функція для пошуку елемента у матриці
def search(mat, element):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == element:
                return i, j

# Функція для шифрування за правилом рядка
def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = matr[e1r][(e1c + 1) % 7]
    char2 = matr[e2r][(e2c + 1) % 7]
    return char1, char2

# Функція для шифрування за правилом стовпця
def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = matr[(e1r + 1) % 5][e1c]
    char2 = matr[(e2r + 1) % 5][e2c]
    return char1, char2

# Функція для шифрування за правилом прямокутника
def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = matr[e1r][e2c]
    char2 = matr[e2r][e1c]
    return char1, char2

# Функція для шифрування за допомогою Playfair Cipher
def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in range(len(plainList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])

        if ele1_x is not None and ele2_x is not None:
            if ele1_x == ele2_x:
                c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            elif ele1_y == ele2_y:
                c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            else:
                c1, c2 = encrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

            cipher = c1 + c2
            CipherText.append(cipher)
    return CipherText

text_Plain = 'Оранжкава це ароматний напій що поєднує смак свіжого апельсинового соку та нотки ароматної кави'
text_Plain = removeSpaces(toLowerCase(text_Plain))
PlainTextList = Diagraph(FillerLetter(text_Plain))
if len(PlainTextList[-1]) != 2:
    PlainTextList[-1] = PlainTextList[-1] + 'з'

key = "код"
print("Ключовий текст:", key)
key = toLowerCase(key)
Matrix = generateKeyTable(key, list1)

print("Таблиця ключа:")
printKeyTable(Matrix)

print("Вихідний текст:", text_Plain)
CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)

CipherText = ""
for i in CipherList:
    CipherText += i
print("Зашифрований текст:", CipherText)

