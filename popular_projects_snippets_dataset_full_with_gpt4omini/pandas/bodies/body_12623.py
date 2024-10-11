# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
from pandas.io.json import dumps

ts = Timestamp("2013-01-10 05:00:00")
exp = '"2013-01-10T05:00:00.000"'

assert dumps(ts, iso_dates=True) == exp
dt = ts.to_pydatetime()
assert dumps(dt, iso_dates=True) == exp
