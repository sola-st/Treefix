# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# GH27172
intervals = [
    Interval(0, 1, closed="left"),
    Interval(1, 2, closed="right"),
    Interval(2, 3, closed="neither"),
    Interval(3, 4, closed="both"),
]
result = Index(intervals)
expected = Index(intervals, dtype=object)
tm.assert_index_equal(result, expected)
