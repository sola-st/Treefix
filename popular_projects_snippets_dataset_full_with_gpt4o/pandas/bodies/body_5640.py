# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
s = Series(Categorical(list("aaabbc")))
result = s.value_counts()
expected = Series([3, 2, 1], index=CategoricalIndex(["a", "b", "c"]))

tm.assert_series_equal(result, expected, check_index_type=True)

# preserve order?
s = s.cat.as_ordered()
result = s.value_counts()
expected.index = expected.index.as_ordered()
tm.assert_series_equal(result, expected, check_index_type=True)
