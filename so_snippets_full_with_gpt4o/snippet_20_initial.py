# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
from l3.Runtime import _l_
try:
    import datetime
    _l_(12409)

except ImportError:
    pass
today = datetime.datetime.now()
_l_(12410)
str(today)
_l_(12411)
'2012-03-14 09:21:58.130922'
_l_(12412)
repr(today)
_l_(12413)
'datetime.datetime(2012, 3, 14, 9, 21, 58, 130922)'
_l_(12414)

