def RLE_algoritm() -> str:
    """Функция на воход получает строку из последовательность символов.
    Обрабатывает на количество повторений и выдает сжатое состояние строки"""

    with open('textTask4.txt', 'r', encoding='UTF-8') as intext:
        data = intext.readline()
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
        with open('text_encoding.txt', 'w', encoding='UTF-8') as outtext:
            outtext.writelines(encoding)
    return encoding
print(RLE_algoritm())


def RLE_decode():
    """Функция на вход получает сжатое состояние строки по методу RLE.
    Обрабатывает количество повторений каждого символа в строке и
    выводит развернутое состояние строки(несжатое)"""
    with open ('text_encoding.txt', 'r', encoding='UTF-8') as text:
        data = text.readline()
        decode = ''
        count = ''
        for char in data:
            if char.isdigit():
                count += char
            else:
                decode += char * int(count)
                count = ''
        with open('text_dencoding.txt', 'w', encoding='UTF-8') as text_decoding:
            text_decoding.writelines(decode)

    return decode
print(RLE_decode())
