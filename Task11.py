#Задание 11-1
import calendar
from datetime import date,datetime

year=int(2023)
free_days = []
for month in range(1, 13):
    counter=0
    for week in calendar.monthcalendar(year, month):
        thursday = week[3]
        if thursday:
            counter+=1
            if counter==3:
                free_days.append(date(year, month, thursday))
                counter=0
result=list(map(lambda x:datetime.strftime(x,'%d.%m.%Y'),free_days))
print(*result,sep='\n')


#Задание11-3
def int_to_roman(num: int) -> str:

    roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                      100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                      10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    roman_num = ''
    for value, numeral in roman_numerals.items():
        while num >= value:
            roman_num += numeral
            num -= value
    return roman_num
print(int_to_roman(int(input())))