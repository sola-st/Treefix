# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
# see gh-7905
idx = DatetimeIndex(data)
assert idx.inferred_freq == expected
