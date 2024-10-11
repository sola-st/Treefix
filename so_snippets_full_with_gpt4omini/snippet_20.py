# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
from l3.Runtime import _l_
try:
    import datetime
    _l_(822)

except ImportError:
    pass
today = datetime.datetime.now()
_l_(823)
str(today)
_l_(824)
'2012-03-14 09:21:58.130922'
_l_(825)
repr(today)
_l_(826)
'datetime.datetime(2012, 3, 14, 9, 21, 58, 130922)'
_l_(827)

