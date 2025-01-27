# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append_common.py
# GH 13524

# same categories -> category
s1 = Series([1, 2, np.nan], dtype="category")
s2 = Series([2, 1, 2], dtype="category")

exp = Series([1, 2, np.nan, 2, 1, 2], dtype="category")
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)

# partially different categories => not-category
s1 = Series([3, 2], dtype="category")
s2 = Series([2, 1], dtype="category")

exp = Series([3, 2, 2, 1])
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)

# completely different categories (same dtype) => not-category
s1 = Series([10, 11, np.nan], dtype="category")
s2 = Series([np.nan, 1, 3, 2], dtype="category")

exp = Series([10, 11, np.nan, np.nan, 1, 3, 2], dtype=np.float64)
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)
