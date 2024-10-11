# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_quarter.py
date = datetime(2012, 3, 31, 5, 30)
result = date + klass()
assert result.time() == date.time()
