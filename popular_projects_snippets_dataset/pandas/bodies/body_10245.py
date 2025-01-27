# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# GH 5869
# datetimelike dtype conversion from int
df = DataFrame({"A": Timestamp("20130101"), "B": np.arange(5)})
expected = df.groupby("A")["A"].apply(lambda x: x.max())
result = df.groupby("A")["A"].max()
tm.assert_series_equal(result, expected)
