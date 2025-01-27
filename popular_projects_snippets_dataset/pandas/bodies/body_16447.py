# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
a = np.random.randint(0, 10, size=50).astype(float)
a[::2] = np.nan
result = cut(
    pd.array(a, dtype="Int64"), bins, right=right, include_lowest=include_lowest
)
expected = cut(a, bins, right=right, include_lowest=include_lowest)
tm.assert_categorical_equal(result, expected)
