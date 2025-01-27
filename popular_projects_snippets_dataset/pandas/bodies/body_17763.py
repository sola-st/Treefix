# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
# see gh-8772
tz = tz_naive_fixture
idx = date_range(date_pair[0], date_pair[1], freq=freq, tz=tz)
assert idx.inferred_freq == freq
