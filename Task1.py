#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def deletion_of_words(find_chars: str) -> str:
    '''Функция получает на вход строку, в которой ищем и удаляем слова в которые входят искомые символы/слова  '''
    with open('text.txt','r', encoding='UTF-8') as inputtext:
        reading_file = inputtext.read()
        text = ' '.join([i for i in reading_file.split() if find_chars not in i])
        with open('text1.txt', 'w', encoding='UTF-8') as outputtext:
            outputtext.writelines(text)

deletion_of_words(find_chars = 'абв')
