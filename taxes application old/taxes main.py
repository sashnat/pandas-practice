# app for calculating taxes
# functions + pandas
# coded by Nataliya Sashnikova


def compare(income):
    i = input('input money, local currency: ')
    j = income(float(i))
    print ('left, $:', j)
    got.append(i)
    input_number.append("i")
    left.append(int(j))
    if len(input_number) >= 3:
        print ('end')
    else:
        return compare(income)


if __name__ == '__main__':
    from taxes_add import income
import pandas as pd
got = []
input_number = []
left = []
compare(income)
df = pd.DataFrame({'input number': [i for i in range(1, len(input_number) + 1)],
                   'local currency got': got,
                   'left, $': left
                  })
df.to_excel('C:\\Users\E277460\PycharmProjects\june 2018\\taxes application\\taxes.xlsx')   # file contains rest of excel files
print(df)

'''
#-----------------------output-------------------------------------------------
input currency exchange: 8
input tax: 18
input money, local currency: 700000
tax, $: 15750.0
left, $: 71750.0
input money, local currency: 800000
tax, $: 18000.0
left, $: 82000.0
input money, local currency: 900000
tax, $: 20250.0
left, $: 92250.0
end
   input number local currency got  left, $
0             1             700000    71750
1             2             800000    82000
2             3             900000    92250

'''
