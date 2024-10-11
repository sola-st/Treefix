# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_concat.py
# we expect the same dtypes as we would get with non-masked inputs,
#  just masked where available.

result = pd.concat([pd.Series([0, 1, pd.NA], dtype=t) for t in to_concat_dtypes])
expected = pd.concat([pd.Series([0, 1, pd.NA], dtype=object)] * 2).astype(
    result_dtype
)
tm.assert_series_equal(result, expected)

# order doesn't matter for result
result = pd.concat(
    [pd.Series([0, 1, pd.NA], dtype=t) for t in to_concat_dtypes[::-1]]
)
expected = pd.concat([pd.Series([0, 1, pd.NA], dtype=object)] * 2).astype(
    result_dtype
)
tm.assert_series_equal(result, expected)
