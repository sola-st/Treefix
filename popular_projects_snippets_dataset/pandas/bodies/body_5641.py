# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
s = Series(Categorical(list("aaaaabbbcc")))  # 4,3,2,1 (nan)
s.iloc[1] = np.nan
result = s.value_counts()
expected = Series(
    [4, 3, 2],
    index=CategoricalIndex(["a", "b", "c"], categories=["a", "b", "c"]),
)
tm.assert_series_equal(result, expected, check_index_type=True)
result = s.value_counts(dropna=False)
expected = Series([4, 3, 2, 1], index=CategoricalIndex(["a", "b", "c", np.nan]))
tm.assert_series_equal(result, expected, check_index_type=True)

# out of order
s = Series(
    Categorical(list("aaaaabbbcc"), ordered=True, categories=["b", "a", "c"])
)
s.iloc[1] = np.nan
result = s.value_counts()
expected = Series(
    [4, 3, 2],
    index=CategoricalIndex(
        ["a", "b", "c"], categories=["b", "a", "c"], ordered=True
    ),
)
tm.assert_series_equal(result, expected, check_index_type=True)

result = s.value_counts(dropna=False)
expected = Series(
    [4, 3, 2, 1],
    index=CategoricalIndex(
        ["a", "b", "c", np.nan], categories=["b", "a", "c"], ordered=True
    ),
)
tm.assert_series_equal(result, expected, check_index_type=True)
