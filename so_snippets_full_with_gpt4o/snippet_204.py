# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
from l3.Runtime import _l_
try:
    from datetime import datetime
    _l_(13651)

except ImportError:
    pass
unixtime = int('1284101485')
_l_(13652)

# Print with local time
print(datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S'))
_l_(13653)

# Print with UTC time
print(datetime.utcfromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S'))
_l_(13654)

