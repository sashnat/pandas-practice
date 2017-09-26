# import os
# path = r'C:\Users\E277460\AppData\Local\Programs\Python\Python36'
# files = os.listdir(path)
# print (files)

import pandas as pd
example = "C:\\Users\E277460\AppData\Local\Programs\Python\Python36\pandas\example.xlsx"
# обязательно укаЗывать \\ для пути файла
df = pd.read_excel(example, sheetname=0)
# or using sheet index starting 0
# или упрощенный вариант,
# если файл в той же директории Python ---- df = pd.read_excel("example.xlsx", sheetname=0)
print (df.head(2)) # выводится только 2 первых ряда без "шапки"
print (df) # массив 
print (df['I']) # значения столбца I
print (df.iloc[1,2]) # 1 - ряд (3-ий, считая "шапку" --> шапка(1)-0(2)-1(3)),
#2 - колонка (3-я --> 0(1)-1(2)-2(3))
# доступ к значению ячейки массива


df.index.name = 'index'
df.index = ['01','02','03','04'] # при переименовании индексов исчезает имя 'index'
df.index.name = 'index_new'
print (df)
print (df['I'])# значения столбца I с новыми индексами
