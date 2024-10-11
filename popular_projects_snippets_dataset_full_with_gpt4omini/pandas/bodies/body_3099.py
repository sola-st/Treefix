# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# shift other axis
# GH#6371
df = DataFrame(np.random.rand(10, 5))
expected = pd.concat(
    [DataFrame(np.nan, index=df.index, columns=[0]), df.iloc[:, 0:-1]],
    ignore_index=True,
    axis=1,
)
result = df.shift(1, axis=1)
tm.assert_frame_equal(result, expected)
