# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_concat.py

result = pd.concat([pd.Series([1, 2, pd.NA], dtype=t) for t in to_concat_dtypes])
expected = pd.concat([pd.Series([1, 2, pd.NA], dtype=object)] * 2).astype(
    result_dtype
)
tm.assert_series_equal(result, expected)
