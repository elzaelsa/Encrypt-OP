def perform_by_type(text, elem_len, cur_len, elem_type):
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


def convert_by_mode(text, connect_symb, cur_len, mode, key):
    if mode == '1':
        # собираем по группам ключа строки в порядке ключа, затем по группам всей строки
        result = connect_symb.join(
            [connect_symb.join([text_part[key.index(str(i))] for i in range(cur_len)]) for text_part in text]
        )
    elif mode == '2':
        # формируем строки по элементам ключа и по группа всей строки
        result = connect_symb.join(
            [connect_symb.join([text_part[int(i)] for i in key]) for text_part in text]
        ).replace('\0', '')

    return result


def encryption(mode, elem_type, elem_len, key, text):
    # символ соединения элементов (для слов пробел)
    connect_symb = ''
    # длина ключа
    cur_len = len(key)

    # преобразовываем текст в зависимости от типа шифровки
    text = perform_by_type(text, elem_len, cur_len, elem_type)

    # разбиваем строку максимальной по длине ключа
    text = [text[i:i + cur_len] for i in range(0, len(text), cur_len)]
    # выбор режима

    return convert_by_mode(text, connect_symb, cur_len, mode, key)


print(encryption(1, 1, 0, ['1', '3', '0', '2'], 'abcdefet'))
