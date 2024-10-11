# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
df = DataFrame([np.arange(10) for x in range(10)])
grouped = df.groupby(0)
result = grouped.mean()
expected = df.groupby(df[0]).mean()
tm.assert_frame_equal(result, expected)
