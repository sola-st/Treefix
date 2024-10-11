from datetime import datetime # pragma: no cover
import pytz # pragma: no cover

class MockPytz: # pragma: no cover
    def timezone(self, name): # pragma: no cover
        if name == 'Asia/India': # pragma: no cover
            name = 'Asia/Kolkata' # pragma: no cover
        return pytz.timezone(name) # pragma: no cover
    @property # pragma: no cover
    def all_timezones(self): # pragma: no cover
        return ['America/New_York', 'Europe/London', 'Asia/Kolkata'] # pragma: no cover
 # pragma: no cover
mock_pytz = MockPytz() # pragma: no cover
tz_India = mock_pytz.timezone('Asia/India') # pragma: no cover
datetime_India = datetime.now(tz_India) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time
from l3.Runtime import _l_
try:
    from datetime import datetime
    _l_(12323)

except ImportError:
    pass
try:
    import pytz
    _l_(12325)

except ImportError:
    pass

tz_NY = pytz.timezone('America/New_York') 
_l_(12326) 
datetime_NY = datetime.now(tz_NY)
_l_(12327)
print("NY time:", datetime_NY.strftime("%H:%M:%S"))
_l_(12328)

tz_London = pytz.timezone('Europe/London')
_l_(12329)
datetime_London = datetime.now(tz_London)
_l_(12330)
print("London time:", datetime_London.strftime("%H:%M:%S"))
_l_(12331)

tz_India = pytz.timezone('Asia/India')
_l_(12332)
datetime_India = datetime.now(tz_India)
_l_(12333)
print("India time:", datetime_India.strftime("%H:%M:%S"))
_l_(12334)

#list timezones
pytz.all_timezones
_l_(12335)

