# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_describe.py
df = DataFrame(
    [[1, 1, 1], [2, 2, 2], [3, 3, 3]],
    columns=["bar", "a", "a"],
    dtype="float64",
)
result = df.describe()
ser = df.iloc[:, 0].describe()
expected = pd.concat([ser, ser, ser], keys=df.columns, axis=1)
tm.assert_frame_equal(result, expected)
