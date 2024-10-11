# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3743222/how-do-i-convert-a-datetime-to-date
from l3.Runtime import _l_
try:
    from datetime import datetime
    _l_(323)

except ImportError:
    pass

#your date-and-time object
# let's supposed it is defined as
datetime_element = datetime(2020, 7, 10, 12, 56, 54, 324893)
_l_(324)

# where
# datetime_element = datetime(year, month, day, hour, minute, second, milliseconds)

# WHAT YOU WANT: your date-only object
date_element = datetime_element.date()
_l_(325)

print(datetime_element)
_l_(326)

print(date_element)
_l_(327)

