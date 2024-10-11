from dateutil import parser # pragma: no cover
import pytz as tz # pragma: no cover

tz = type('MockTZ', (object,), {'tzlocal': staticmethod(lambda: pytz.timezone('UTC'))})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7065164/how-to-make-a-timezone-aware-datetime-object
from l3.Runtime import _l_
unaware=parser.parse("2020-05-01 0:00:00")
_l_(1815)
aware=unaware.replace(tzinfo=tz.tzlocal()).astimezone(tz.tzlocal())
_l_(1816)

