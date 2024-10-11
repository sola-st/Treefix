# Extracted from ./data/repos/pandas/pandas/tests/series/test_reductions.py
ser = Series([1.0, 1.0, 1.0], index=range(3))
result = ser.prod()

assert not isinstance(result, Series)
