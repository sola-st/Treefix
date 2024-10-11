# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
# see gh-6407
s = Series(date_range("20130101", "20130110"))
inferred = frequencies.infer_freq(s)
assert inferred == "D"
