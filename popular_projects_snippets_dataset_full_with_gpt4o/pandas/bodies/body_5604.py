# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# 9346
# light testing of guarantee of order of appearance
# these also are the doc-examples
result = pd.unique(Series([2, 1, 3, 3]))
tm.assert_numpy_array_equal(result, np.array([2, 1, 3], dtype="int64"))

result = pd.unique(Series([2] + [1] * 5))
tm.assert_numpy_array_equal(result, np.array([2, 1], dtype="int64"))

result = pd.unique(Series([Timestamp("20160101"), Timestamp("20160101")]))
expected = np.array(["2016-01-01T00:00:00.000000000"], dtype="datetime64[ns]")
tm.assert_numpy_array_equal(result, expected)

result = pd.unique(
    Index(
        [
            Timestamp("20160101", tz="US/Eastern"),
            Timestamp("20160101", tz="US/Eastern"),
        ]
    )
)
expected = DatetimeIndex(
    ["2016-01-01 00:00:00"], dtype="datetime64[ns, US/Eastern]", freq=None
)
tm.assert_index_equal(result, expected)

result = pd.unique(list("aabc"))
expected = np.array(["a", "b", "c"], dtype=object)
tm.assert_numpy_array_equal(result, expected)

result = pd.unique(Series(Categorical(list("aabc"))))
expected = Categorical(list("abc"))
tm.assert_categorical_equal(result, expected)
