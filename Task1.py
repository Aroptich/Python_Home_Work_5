#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def deletion_of_words(text: str, find_chars: str) -> str:
    '''Функция получает на вход строку, в которой ищем и удаляем слова в которые входят искомые символы/слова  '''
    return ' '.join([i for i in text.split() if find_chars not in i])
print(deletion_of_words(text='проибабвшцуоашц дацоашуоц вйлцвлйцхабвд лащула',
                  find_chars = 'абв'))
