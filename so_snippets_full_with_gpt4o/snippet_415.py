# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13890935/does-pythons-time-time-return-the-local-or-utc-timestamp
from l3.Runtime import _l_
try:
    import datetime
    _l_(13970)

except ImportError:
    pass

local_time = datetime.datetime.now()
_l_(13971)
print(local_time.strftime('%Y%m%d %H%M%S'))
_l_(13972)

utc_time = datetime.datetime.utcnow() 
_l_(13973) 
print(utc_time.strftime('%Y%m%d %H%M%S'))
_l_(13974)

