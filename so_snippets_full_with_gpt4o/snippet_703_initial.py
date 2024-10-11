# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/30071886/how-to-get-current-time-in-python-and-break-up-into-year-month-day-hour-minu
from l3.Runtime import _l_
try:
    import time
    _l_(13263)

except ImportError:
    pass
year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())
_l_(13264)

