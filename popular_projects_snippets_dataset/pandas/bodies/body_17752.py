# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
index = DatetimeIndex(["1/1/2000", "1/2/2000", "1/3/2000"])
assert frequencies.infer_freq(index) == "D"
