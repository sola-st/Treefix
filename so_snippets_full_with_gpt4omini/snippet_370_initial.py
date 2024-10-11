# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
from l3.Runtime import _l_
def ordinal(year, month, day):
    _l_(2995)

    aux = ((year-1)*365 + (year-1)//4 - (year-1)//100 + (year-1)//400
         + [ 0,31,59,90,120,151,181,212,243,273,304,334][month - 1]
         + day
         + int(((year%4==0 and year%100!=0) or year%400==0) and month > 2))
    _l_(2994)
    return aux

print(ordinal(2021, 5, 10) - ordinal(2001, 9, 11))
_l_(2996)

