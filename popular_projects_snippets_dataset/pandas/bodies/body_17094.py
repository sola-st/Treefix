# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append_common.py
# GH 13524

s1 = Series(Categorical([1, 2, np.nan], ordered=True))
s2 = Series(Categorical([2, 1, 2], ordered=True))

exp = Series(Categorical([1, 2, np.nan, 2, 1, 2], ordered=True))
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)

exp = Series(Categorical([1, 2, np.nan, 2, 1, 2, 1, 2, np.nan], ordered=True))
tm.assert_series_equal(pd.concat([s1, s2, s1], ignore_index=True), exp)
tm.assert_series_equal(s1._append([s2, s1], ignore_index=True), exp)
