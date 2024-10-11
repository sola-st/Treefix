# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
# see gh-7310
tz = tz_naive_fixture
idx = DatetimeIndex(dates, tz=tz)
assert idx.inferred_freq == expected
