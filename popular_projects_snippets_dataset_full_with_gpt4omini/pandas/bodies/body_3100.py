# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# shift named axis
df = DataFrame(np.random.rand(10, 5))
expected = pd.concat(
    [DataFrame(np.nan, index=df.index, columns=[0]), df.iloc[:, 0:-1]],
    ignore_index=True,
    axis=1,
)
result = df.shift(1, axis="columns")
tm.assert_frame_equal(result, expected)
