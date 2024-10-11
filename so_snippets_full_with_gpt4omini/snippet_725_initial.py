# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10624937/convert-datetime-object-to-a-string-of-date-only-in-python
from l3.Runtime import _l_
try:
    from datetime import datetime
    _l_(3224)

except ImportError:
    pass

date_time = datetime(2012, 2, 23, 0, 0)
_l_(3225)
date = date_time.strftime('%m/%d/%Y')
_l_(3226)
print("date: %s" % date)
_l_(3227)

