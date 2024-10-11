# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
from l3.Runtime import _l_
try:
    import datetime, time
    _l_(230)

except ImportError:
    pass
ls = ['31/1/2007', '14/2/2017']
_l_(231)
for d in ls:
    _l_(235)

    dt = datetime.datetime.strptime(d, "%d/%m/%Y")
    _l_(232)
    print(dt)
    _l_(233)
    print(dt.strftime("%A"))
    _l_(234)

