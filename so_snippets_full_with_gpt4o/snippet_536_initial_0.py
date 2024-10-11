from datetime import datetime # pragma: no cover

start_date = datetime(2023, 1, 1) # pragma: no cover
delta_period = 3 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/546321/how-do-i-calculate-the-date-six-months-from-the-current-date-using-the-datetime
from l3.Runtime import _l_
try:
    from datetime import timedelta
    _l_(12790)

except ImportError:
    pass
try:
    from dateutil.relativedelta import relativedelta
    _l_(12792)

except ImportError:
    pass

end_date = start_date + relativedelta(months=delta_period) + timedelta(days=-delta_period)
_l_(12793)

