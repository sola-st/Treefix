# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
# GH21956
df = DataFrame({"A": [np.nan, np.nan], "B": ["a", "b"], "C": [1, 2]})
result = df.groupby(["A", "B"]).C.count()
mi = MultiIndex(levels=[[], ["a", "b"]], codes=[[], []], names=["A", "B"])
expected = Series([], index=mi, dtype=np.int64, name="C")
tm.assert_series_equal(result, expected, check_index_type=False)
