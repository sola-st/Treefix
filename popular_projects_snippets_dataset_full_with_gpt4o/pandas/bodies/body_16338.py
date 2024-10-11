# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH19018
# initialization ordering: by insertion order if python>= 3.6, else
# order by value
d = {"b": 1, "a": 0, "c": 2}
result = Series(d)
expected = Series([1, 0, 2], index=list("bac"))
tm.assert_series_equal(result, expected)
