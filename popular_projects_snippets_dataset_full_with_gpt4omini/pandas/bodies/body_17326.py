# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
indices = [1, 5, -2, 6, 3, -1]
df = tm.makeTimeDataFrame()
out = df.take(indices)
expected = DataFrame(
    data=df.values.take(indices, axis=0),
    index=df.index.take(indices),
    columns=df.columns,
)
tm.assert_frame_equal(out, expected)
