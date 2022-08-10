# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import os
path1 = os.path.join('PythonHW05', 'ex01', 'input1.txt')
with open(path1, 'r') as my_file:
    data1 = my_file.readline()
data1 = data1.split()
print(data1)



def del_some_words(my_text):
    my_text = list(
        filter(lambda x: 'абв' not in x, my_text))
    return " ".join(my_text)


my_text = del_some_words(data1)
print(my_text)
