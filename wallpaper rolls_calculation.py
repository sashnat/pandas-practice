# coded by Nataliya Sashnikova
# Расчет рулонов обоев


import math
from functools import reduce
import pandas as pd
import numpy as np

h_roll = float(input('высота (длина) рулона/ roll  height: '))
w_roll = float(input('ширина рулона/ roll width: '))


def calc():
    global i
    i += 1
    h_area = float(input('высота участка/ area height: '))
    w_area = float(input('ширина участка/ area width: '))
    pcs_num = math.floor(h_roll/h_area)                                             # целых кусков (полос) для одного рулона/ pieces q-ty for a roll
    roll_num = math.ceil(math.ceil(w_area/w_roll)/math.floor(h_roll/h_area))        # количество рулонов/ rolls q-ty
    spare_pcs_num = roll_num*math.floor(h_roll/h_area)-math.ceil(w_area/w_roll)     # в резерве полос для участка/ spare pieces for the area
    spare_metr = h_roll - h_area*(math.floor(h_roll/h_area ))                       # в резерве (метров) для одного рулона/ spare (metres/ inches) for one roll
    spare_metr_sum = h_roll*roll_num - h_area*roll_num*(math.floor(h_roll/h_area )) # в резерве (метров) для всех рулонов/ spare (metres/ inches) for roll for the area

    sum_roll_num.append(roll_num)
    sum_spare.append(spare_metr_sum)
    d[i] = {"roll_num": roll_num, "h_area": h_area, "pcs_num": pcs_num, "spare_pcs_num": spare_pcs_num, "spare_metr": spare_metr, "spare_metr_sum": spare_metr_sum}
    answer = input('want another entry: (y/n) ?').lower()
    if answer == 'y':
        return calc()
    else:
        print('get result')
    return roll_num


d = {}
sum_roll_num = []
sum_spare = []
i = 0
calc()

print("всего рулонов, шт./ rolls in sum req :", reduce((lambda x, y: x + y), sum_roll_num))
print("всего резерв, м / spare in sum:", reduce((lambda x, y: x + y), sum_spare))

df = pd.DataFrame({'area number': [key for key in d],
                   'h_area': [d[key]['h_area'] for key in d],
                   'roll_num': [d[key]['roll_num'] for key in d],
                   'pcs_num': [d[key]['pcs_num'] for key in d],
                   'spare_pcs_num': [d[key]['spare_pcs_num'] for key in d],
                   'spare_metr': [d[key]['spare_metr'] for key in d],
                   'spare_metr_sum': [d[key]['spare_metr_sum'] for key in d]
                  })


# to find out if there is a spare in an area that can be used for another area. If it's so, it prints "yes"
def df_x():
    global x
    q = df.loc[x, 'h_area']
    df['spare can be used for ' + str(x + 1) + ' area'] = ["yes" if q <= df.loc[i, 'spare_metr'] and df.loc[x, 'roll_num'] <= df.loc[i, 'roll_num'] else 'N/A' for i in range(len(df.index))]
    return df['spare can be used for ' + str(x + 1) + ' area']


for x in range(len(df.index)):
    df_x()


df.index = (str(i) + '- area' for i in range(1, len(df.index) + 1))
stacked = df.stack()
print(stacked)

df.to_excel('C:\\Users\E277460\PycharmProjects\june 2018\\calculation of wallpaper rolls\\calc1.xlsx')
stacked.to_excel('C:\\Users\E277460\PycharmProjects\june 2018\\calculation of wallpaper rolls\\stacked1.xlsx')


#---------------------Output---------------- :
'''
высота (длина) рулона/ roll  height: 10
ширина рулона/ roll width: 5
высота участка/ area height: 2.75
ширина участка/ area width: 4
want another entry: (y/n) ?y
высота участка/ area height: 1.25
ширина участка/ area width: 4
want another entry: (y/n) ?y
высота участка/ area height: 1
ширина участка/ area width: 4
want another entry: (y/n) ?n
get result
всего рулонов, шт./ rolls in sum req : 3
всего резерв, м / spare in sum: 1.75
1- area  area number                        1
         h_area                          2.75
         roll_num                           1
         pcs_num                            3
         spare_pcs_num                      2
         spare_metr                      1.75
         spare_metr_sum                  1.75
         spare can be used for 1 area     N/A
         spare can be used for 2 area     yes
         spare can be used for 3 area     yes
2- area  area number                        2
         h_area                          1.25
         roll_num                           1
         pcs_num                            8
         spare_pcs_num                      7
         spare_metr                         0
         spare_metr_sum                     0
         spare can be used for 1 area     N/A
         spare can be used for 2 area     N/A
         spare can be used for 3 area     N/A
3- area  area number                        3
         h_area                             1
         roll_num                           1
         pcs_num                           10
         spare_pcs_num                      9
         spare_metr                         0
         spare_metr_sum                     0
         spare can be used for 1 area     N/A
         spare can be used for 2 area     N/A
         spare can be used for 3 area     N/A
dtype: object

'''
