# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append_common.py
# GH 13524

s1 = Series([], dtype="category")
s2 = Series([1, 2], dtype="category")

tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), s2)
tm.assert_series_equal(s1._append(s2, ignore_index=True), s2)

tm.assert_series_equal(pd.concat([s2, s1], ignore_index=True), s2)
tm.assert_series_equal(s2._append(s1, ignore_index=True), s2)

s1 = Series([], dtype="category")
s2 = Series([], dtype="category")

tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), s2)
tm.assert_series_equal(s1._append(s2, ignore_index=True), s2)

s1 = Series([], dtype="category")
s2 = Series([], dtype="object")

# different dtype => not-category
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), s2)
tm.assert_series_equal(s1._append(s2, ignore_index=True), s2)
tm.assert_series_equal(pd.concat([s2, s1], ignore_index=True), s2)
tm.assert_series_equal(s2._append(s1, ignore_index=True), s2)

s1 = Series([], dtype="category")
s2 = Series([np.nan, np.nan])

# empty Series is ignored
exp = Series([np.nan, np.nan])
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)

tm.assert_series_equal(pd.concat([s2, s1], ignore_index=True), exp)
tm.assert_series_equal(s2._append(s1, ignore_index=True), exp)
