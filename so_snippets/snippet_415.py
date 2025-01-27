# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13890935/does-pythons-time-time-return-the-local-or-utc-timestamp
from l3.Runtime import _l_
try:
    import datetime
    _l_(1797)

except ImportError:
    pass

local_time = datetime.datetime.now()
_l_(1798)
print(local_time.strftime('%Y%m%d %H%M%S'))
_l_(1799)

utc_time = datetime.datetime.utcnow() 
_l_(1800) 
print(utc_time.strftime('%Y%m%d %H%M%S'))
_l_(1801)

