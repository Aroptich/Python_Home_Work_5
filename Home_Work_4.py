 def RLE_algoritm(data):
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
#     else:
#         encoding += str(count) + previous_character
#         return encoding
#
#
# print(RLE_algoritm('wwwwiiiiJJJ;;;TTTuudddccbv'))
#
# def RLE_decode(data):
#     decode = ''
#     count = ''
#     for char in data:
#         if char.isdigit():
#             count += char
#         else:
#             decode += char * int(count)
#             count = ''
#     return decode
# print(RLE_decode(RLE_algoritm('wwwwiiiiJJJ;;;TTTuudddccbv')))
