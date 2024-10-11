# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
from l3.Runtime import _l_
try:
    from datetime import date
    _l_(12029)

except ImportError:
    pass
today = date.today().isoformat()
_l_(12030)
print(today)  # '2018-12-05'
_l_(12031)  # '2018-12-05'
try:
    from datetime import datetime
    _l_(12033)

except ImportError:
    pass
now = datetime.today().isoformat()
_l_(12034)
print(now)  # '2018-12-05T11:15:55.126382'
_l_(12035)  # '2018-12-05T11:15:55.126382'

