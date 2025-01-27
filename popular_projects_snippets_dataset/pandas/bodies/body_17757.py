# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
rng = DatetimeIndex(["1/31/2000", "2/29/2000", "3/31/2000"])
assert rng.inferred_freq == "M"
