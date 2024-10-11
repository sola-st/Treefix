# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
result = cut(
    date_range("20130102", periods=5), bins=date_range("20130101", periods=2)
)

mask = result.categories.isna()
tm.assert_numpy_array_equal(mask, np.array([False]))

mask = result.isna()
tm.assert_numpy_array_equal(mask, np.array([False, True, True, True, True]))
