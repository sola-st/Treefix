# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
rng = DatetimeIndex(["1/31/2000", "1/31/2001", "1/31/2002"])
assert rng.inferred_freq == "A-JAN"
