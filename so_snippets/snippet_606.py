# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
from l3.Runtime import _l_
try:
    from datetime import date,timedelta
    _l_(2825)

except ImportError:
    pass
delta = timedelta(days=1)
_l_(2826)
start = date(2020,1,1)
_l_(2827)
end=date(2020,9,1)
_l_(2828)
loop_date = start
_l_(2829)
while loop_date<=end:
    _l_(2832)

    print(loop_date)
    _l_(2830)
    loop_date+=delta
    _l_(2831)

