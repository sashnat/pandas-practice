# put in practice some python skills :)) :
def me(ya):
    print("Я, " + ya + ", хочу в отпуск")
    def tr0():
        q = input("Давай сыграем, если выиграешь, пойдешь в отпуск. Ok?:) ").lower()
        def tr():
           if q in s:
                b = input("Как пишется слон на английском языке?").lower()
                i.append(str(1))
                if b == "elephant":
                    print("Поздравляю! Ты уходишь в отпуск!" + \
                          " Осталось только написать заявление на отпуск." + \
                          " Форма здесь")
                    vac_form = r'C:\\Users\E277460\PycharmProjects\Jupyter\exercise_1\vac_form.xlsx'
                    df_n = pd.read_excel(r'C:\\Users\E277460\PycharmProjects\Jupyter\exercise_1\\vac_form - Copy.xlsx')

                    book = load_workbook(vac_form)
                    writer = pd.ExcelWriter(vac_form, engine='openpyxl') # writes into a new sheet
                    writer.book = book

                    df_n.ix[0, 2] = ya if ya == "Natalya Sashnikova" else input("введите свое имя: ")
                    df_n.ix[5, 2] = input("введите дату: ")

                    print(df_n)
                    df_n.head(100)

                    df_n.to_excel(writer, sheet_name = "New", index = False )
                    writer.save()
                    print ("Хорошего отпуска !!!! ")


                else:
                    if len(i) >= 3:
                        print ('Sorry ... Зайдите попозже, поиграем :)')
                        return
                    else:
                        print ('К сожалению, неправильно, попробуем еще раз !')
                        return tr()
                        
           else:
               print ("по-английски, пожалуйста, попробуем еще раз")
               print (tr0())
        print (tr())

    print(tr0())

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from openpyxl import load_workbook

import os

i = []
s = ['ok', 'yes', 'sure', 'yeap']
me(input("what is your name?"))
''' 
----------------------Output-----------------------------------

what is your name?m
Я, m, хочу в отпуск
Давай сыграем, если выиграешь, пойдешь в отпуск. Ok?:)ok
Как пишется слон на английском языке?elephant
Поздравляю! Ты уходишь в отпуск! Осталось только написать заявление на отпуск. Форма здесь
введите свое имяME
введите дату:20_12_17
   Unnamed: 0            Unnamed: 1 Unnamed: 2
0         NaN                   NaN         ME
1         NaN  Заявление на отпуск   Заявитель
2         NaN                   NaN        NaN
3         NaN                   NaN        NaN
4         NaN                   NaN        NaN
5         NaN                   NaN   20_12_17
6         NaN                   NaN       дата
Хорошего отпуска !!!! 
'''



