from datetime import datetime # pragma: no cover
from dateutil.relativedelta import relativedelta # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python
from l3.Runtime import _l_
try:
        import datetime as dt
        _l_(1346)

except ImportError:
        pass
try:
        from dateutil.relativedelta import relativedelta
        _l_(1348)

except ImportError:
        pass

def month_range(start_date, n_months):
        _l_(1351)

        for m in range(n_months):
                _l_(1350)

                yield start_date + relativedelta(months=+m)
                _l_(1349)

