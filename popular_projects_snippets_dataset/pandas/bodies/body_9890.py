# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH 42064 46431

sr = Series([1 / 3, 4, 0, 0, 0, 0, 0])
r = sr.rolling(4)
result = r.skew()
assert (result[-2:] == 0).all()
result = r.kurt()
assert (result[-2:] == -3).all()
