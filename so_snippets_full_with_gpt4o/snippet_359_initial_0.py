from dateutil import parser # pragma: no cover
from dateutil import tz # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7065164/how-to-make-a-timezone-aware-datetime-object
from l3.Runtime import _l_
unaware=parser.parse("2020-05-01 0:00:00")
_l_(13986)
aware=unaware.replace(tzinfo=tz.tzlocal()).astimezone(tz.tzlocal())
_l_(13987)

