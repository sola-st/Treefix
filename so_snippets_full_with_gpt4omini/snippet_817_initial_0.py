import datetime # pragma: no cover

my_dt = datetime.datetime(2023, 1, 1, 12, 0, 0) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/79797/how-to-convert-local-time-string-to-utc
from l3.Runtime import _l_
datetime.datetime.utcfromtimestamp(my_dt.timestamp())
_l_(1677)

