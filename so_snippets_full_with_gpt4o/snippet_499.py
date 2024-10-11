# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2150739/iso-time-iso-8601-in-python
from l3.Runtime import _l_
tz = str.format('{0:+06.2f}', float(time.altzone) / 3600)
_l_(12992)

tz = str.format('{0:+06.2f}', -float(time.altzone) / 3600)
_l_(12993)

