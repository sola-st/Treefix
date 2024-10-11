# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
grouped = df.groupby(["A", "B"])["C"]

agged = grouped.agg([np.mean, np.std])
expected = DataFrame({"mean": grouped.agg(np.mean), "std": grouped.agg(np.std)})
tm.assert_frame_equal(agged, expected)
