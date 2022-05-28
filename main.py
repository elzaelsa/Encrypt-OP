def perform_by_type(text, elem_len, cur_len):
    if elem_type == '1' or elem_len == '1':
        # длина хвоста без группировки
        ost_len = len(text) % cur_len
        # добавляем недостающие элементы
        text += ((cur_len - ost_len) % cur_len) * '\0'
    elif elem_type == '2':
        # длина блока
        elem_len = int(elem_len)
        # добавляем недостающие элементы и формируем список из строки по группам
        text += (cur_len * elem_len - len(text)) * '\0'
        text = [text[i:i + elem_len] for i in range(0, len(text), elem_len)]
    elif elem_type == '3':
        # меняем соед. символ для слов и разбиваем строку по пробелам
        connect_symb = ' '
        text = text.split()
        # считаем хвост и добавляем в список элементами \0
        ost_len = len(text) % cur_len
        text += ['\0' for _ in range((cur_len - ost_len) % cur_len)]

    return text


def convert_by_mode(text, connect_symb, cur_len):
    if mode == '1':
        # собираем по группам ключа строки в порядке ключа, затем по группам всей строки
        result = connect_symb.join(
            [connect_symb.join([text_part[key.index(str(i))] for i in range(cur_len)]) for text_part in text])
    elif mode == '2':
        # формируем строки по элементам ключа и по группа всей строки
        result = connect_symb.join([connect_symb.join([text_part[int(i)] for i in key]) for text_part in text]).replace(
            '\0', '')

    return result


def encryption(mode, elem_type, elem_len, key, text):
    # символ соединения элементов (для слов пробел)
    connect_symb = ''
    # длина ключа
    cur_len = len(key)

    # преобразовываем текст в зависимости от типа шифровки
    text = perform_by_type(text, elem_len, cur_len)

    # разбиваем строку максимальной по длине ключа
    text = [text[i:i + cur_len] for i in range(0, len(text), cur_len)]
    # выбор режима

    return convert_by_mode(text, connect_symb, cur_len)


def is_valid_key(key):
    for k in key:
        if not k.isdigit() or len(k) > 1:
            return False
    return True


# Реализация Меню
print('Меню:', '1. Шифрование', '2. Разшифровывание', end='\n')
mode = input('Выберите режим: ')
# Обработка некорректного ввода
while mode not in ('1', '2'):
    mode = input('Пожалуйста, выберите один из вариантов: ')
print('Виды элемента:', '1. Один символ', '2. Группа символов', '3. Слово', end='\n')
elem_type = input('Выберите вид элемента: ')
# Обработка некорректного ввода
while elem_type not in ('1', '2', '3'):
    elem_type = input('Пожалуйста, выберите один из вариантов: ')
if elem_type == '2':
    elem_len = input('Введите длину блока: ')
    # Обработка некорректного ввода
    while not elem_len.isdigit():
        elem_len = input('Пожалуйста, введите корректное значение: ')
else:
    elem_len = ''
key = input('Введите ключ (через пробел, например - 3 0 2 1):').split(' ')
# Обработка некорректного ввода
while not is_valid_key(key):
    key = input('Пожалуйста, введите корректное значение (например - 3 0 2 1): ').split(' ')
text = input('Введите сообщение: ')

# шифрование/дешифрование и вывод
result = encryption(mode, elem_type, elem_len, key, text)
print(f'\nРезультат: {result}')