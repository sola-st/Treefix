# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 23563: mixed closed results in object dtype (not interval dtype)
data = [Interval(0, 1, closed="both"), Interval(0, 2, closed="neither")]
result = Series(data_constructor(data))
assert result.dtype == object
assert result.tolist() == data
