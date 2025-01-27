# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
from pandas.io.json import dumps

exp = '"2013-01-10T05:00:00.000Z"'

assert dumps(ts, iso_dates=True) == exp
dt = ts.to_pydatetime()
assert dumps(dt, iso_dates=True) == exp
