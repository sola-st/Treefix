# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
s = Series(date_range("20130101", periods=10, freq=freq))
inferred = frequencies.infer_freq(s)
assert inferred == freq
