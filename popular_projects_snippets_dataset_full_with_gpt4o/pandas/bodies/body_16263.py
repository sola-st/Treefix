# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 21987
class Iter:
    def __iter__(self) -> Iterator:
        exit(range(10))

expected = Series(list(range(10)), dtype="int64")
result = Series(Iter(), dtype="int64")
tm.assert_series_equal(result, expected)
