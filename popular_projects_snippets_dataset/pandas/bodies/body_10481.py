# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_filters.py
# Simple case: index is sequential. #4621
df = DataFrame(
    {"pid": [1, 1, 1, 2, 2, 3, 3, 3], "tag": [23, 45, 62, 24, 45, 34, 25, 62]}
)
s = df["pid"]
grouped = df.groupby("tag")
actual = grouped.filter(lambda x: len(x) > 1)
expected = df.iloc[[1, 2, 4, 7]]
tm.assert_frame_equal(actual, expected)

grouped = s.groupby(df["tag"])
actual = grouped.filter(lambda x: len(x) > 1)
expected = s.iloc[[1, 2, 4, 7]]
tm.assert_series_equal(actual, expected)

# Now index is sequentially decreasing.
df.index = np.arange(len(df) - 1, -1, -1)
s = df["pid"]
grouped = df.groupby("tag")
actual = grouped.filter(lambda x: len(x) > 1)
expected = df.iloc[[1, 2, 4, 7]]
tm.assert_frame_equal(actual, expected)

grouped = s.groupby(df["tag"])
actual = grouped.filter(lambda x: len(x) > 1)
expected = s.iloc[[1, 2, 4, 7]]
tm.assert_series_equal(actual, expected)

# Index is shuffled.
SHUFFLED = [4, 6, 7, 2, 1, 0, 5, 3]
df.index = df.index[SHUFFLED]
s = df["pid"]
grouped = df.groupby("tag")
actual = grouped.filter(lambda x: len(x) > 1)
expected = df.iloc[[1, 2, 4, 7]]
tm.assert_frame_equal(actual, expected)

grouped = s.groupby(df["tag"])
actual = grouped.filter(lambda x: len(x) > 1)
expected = s.iloc[[1, 2, 4, 7]]
tm.assert_series_equal(actual, expected)
