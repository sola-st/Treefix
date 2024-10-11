# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
df = DataFrame(
    np.arange(1, 10, dtype="f8").reshape(3, 3),
    columns=["one", "two", "three"],
    index=["a", "b", "c"],
)

val1 = df.xs("a").values
added = DataFrame(df.values + val1, index=df.index, columns=df.columns)
tm.assert_frame_equal(df + val1, added)

added = DataFrame((df.values.T + val1).T, index=df.index, columns=df.columns)
tm.assert_frame_equal(df.add(val1, axis=0), added)

val2 = list(df["two"])

added = DataFrame(df.values + val2, index=df.index, columns=df.columns)
tm.assert_frame_equal(df + val2, added)

added = DataFrame((df.values.T + val2).T, index=df.index, columns=df.columns)
tm.assert_frame_equal(df.add(val2, axis="index"), added)

val3 = np.random.rand(*df.shape)
added = DataFrame(df.values + val3, index=df.index, columns=df.columns)
tm.assert_frame_equal(df.add(val3), added)
