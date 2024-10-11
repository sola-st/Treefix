# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_reindex.py
# GH 42424
ci = CategoricalIndex(
    [Interval(0, 1, closed="right"), Interval(1, 2, closed="right")],
    ordered=True,
)
ci_add = CategoricalIndex(
    [
        Interval(0, 1, closed="right"),
        Interval(1, 2, closed="right"),
        Interval(2, 3, closed="right"),
        Interval(3, 4, closed="right"),
    ],
    ordered=True,
)
result, _ = ci.reindex(ci_add)
expected = ci_add
tm.assert_index_equal(expected, result)
