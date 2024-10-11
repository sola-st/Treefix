# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
off = BDay(1, offset=timedelta(0, 1800))
assert off.freqstr == "B+30Min"

off = BDay(1, offset=timedelta(0, -1800))
assert off.freqstr == "B-30Min"
