def RLE_algoritm(data: str) -> str:
    """Функция на воход получает строку из последовательность символов.
    Обрабатывает на количество повторений и выдает сжатое состояние строки"""
    encoding = ''
    previous_character = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != previous_character:
            if previous_character:
                encoding += str(count) + previous_character
            count = 1
            previous_character = char
        else:
            count += 1

    else:
        encoding += str(count) + previous_character
    return encoding

print(RLE_algoritm('wwwwiiiiJJJ;;;TTTuudddccbv'))


def RLE_decode(data):
    """Функция на вход получает сжатое состояние строки по методу RLE.
    Обрабатывает количество повторений каждого символа в строке и
    выводит развернутое состояние строки(несжатое)"""
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


print(RLE_decode(RLE_algoritm('wwwwiiiiJJJ;;;TTTuudddccbv')))
