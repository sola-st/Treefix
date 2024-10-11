# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
s = Series(Categorical([1, 2, np.nan, np.nan]))
result = s.mode(dropna)
expected1 = Series(expected1, dtype="category")
tm.assert_series_equal(result, expected1)

s = Series(Categorical([1, "a", "a", np.nan, np.nan]))
result = s.mode(dropna)
expected2 = Series(expected2, dtype="category")
tm.assert_series_equal(result, expected2)

s = Series(
    Categorical(
        [1, 1, 2, 3, 3, np.nan, np.nan], categories=[3, 2, 1], ordered=True
    )
)
result = s.mode(dropna)
expected3 = Series(expected3, dtype="category")
tm.assert_series_equal(result, expected3)
