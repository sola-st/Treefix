# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
from l3.Runtime import _l_
try:
    import datetime, time
    _l_(12132)

except ImportError:
    pass
ls = ['31/1/2007', '14/2/2017']
_l_(12133)
for d in ls:
    _l_(12137)

    dt = datetime.datetime.strptime(d, "%d/%m/%Y")
    _l_(12134)
    print(dt)
    _l_(12135)
    print(dt.strftime("%A"))
    _l_(12136)

