# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# https://github.com/pandas-dev/pandas/issues/9443#issuecomment-73719328

tm.assert_series_equal(
    Series([True, True, False]).value_counts(dropna=True),
    Series([2, 1], index=[True, False]),
)
tm.assert_series_equal(
    Series([True, True, False]).value_counts(dropna=False),
    Series([2, 1], index=[True, False]),
)

tm.assert_series_equal(
    Series([True] * 3 + [False] * 2 + [None] * 5).value_counts(dropna=True),
    Series([3, 2], index=Index([True, False], dtype=object)),
)
tm.assert_series_equal(
    Series([True] * 5 + [False] * 3 + [None] * 2).value_counts(dropna=False),
    Series([5, 3, 2], index=[True, False, np.nan]),
)
tm.assert_series_equal(
    Series([10.3, 5.0, 5.0]).value_counts(dropna=True),
    Series([2, 1], index=[5.0, 10.3]),
)
tm.assert_series_equal(
    Series([10.3, 5.0, 5.0]).value_counts(dropna=False),
    Series([2, 1], index=[5.0, 10.3]),
)

tm.assert_series_equal(
    Series([10.3, 5.0, 5.0, None]).value_counts(dropna=True),
    Series([2, 1], index=[5.0, 10.3]),
)

result = Series([10.3, 10.3, 5.0, 5.0, 5.0, None]).value_counts(dropna=False)
expected = Series([3, 2, 1], index=[5.0, 10.3, np.nan])
tm.assert_series_equal(result, expected)
