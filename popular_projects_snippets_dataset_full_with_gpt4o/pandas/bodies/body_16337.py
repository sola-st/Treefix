# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 18625
d = {"a": [[2], [3], [4]]}
result = Series(d, index=["a"], dtype="object")
expected = Series(d, index=["a"])
tm.assert_series_equal(result, expected)
