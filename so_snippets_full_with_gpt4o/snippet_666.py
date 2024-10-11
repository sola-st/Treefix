# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2803852/python-date-string-to-date-object
from l3.Runtime import _l_
try:
    import datetime
    _l_(14959)

except ImportError:
    pass
datetime.datetime.strptime('24052010', "%d%m%Y").date()
_l_(14960)
datetime.date(2010, 5, 24)
_l_(14961)

