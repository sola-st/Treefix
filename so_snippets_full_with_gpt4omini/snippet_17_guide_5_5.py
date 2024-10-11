from datetime import datetime # pragma: no cover
import pytz # pragma: no cover

tz_India = pytz.timezone('Asia/Kolkata') # pragma: no cover
datetime_India = datetime.now(tz_India) # pragma: no cover
print('India time:', datetime_India.strftime('%H:%M:%S')) # pragma: no cover
all_timezones = ['America/New_York', 'Europe/London', 'Asia/Kolkata'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time
from l3.Runtime import _l_
try:
    from datetime import datetime
    _l_(666)

except ImportError:
    pass
try:
    import pytz
    _l_(668)

except ImportError:
    pass

tz_NY = pytz.timezone('America/New_York') 
_l_(669) 
datetime_NY = datetime.now(tz_NY)
_l_(670)
print("NY time:", datetime_NY.strftime("%H:%M:%S"))
_l_(671)

tz_London = pytz.timezone('Europe/London')
_l_(672)
datetime_London = datetime.now(tz_London)
_l_(673)
print("London time:", datetime_London.strftime("%H:%M:%S"))
_l_(674)

tz_India = pytz.timezone('Asia/India')
_l_(675)
datetime_India = datetime.now(tz_India)
_l_(676)
print("India time:", datetime_India.strftime("%H:%M:%S"))
_l_(677)

#list timezones
pytz.all_timezones
_l_(678)

