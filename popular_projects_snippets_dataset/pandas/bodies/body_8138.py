# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH27172
intervals = [
    pd.Interval(0, 1, closed="left"),
    pd.Interval(1, 2, closed="right"),
    pd.Interval(2, 3, closed="neither"),
    pd.Interval(3, 4, closed="both"),
]
result = ensure_index(intervals)
expected = Index(intervals, dtype=object)
tm.assert_index_equal(result, expected)
