# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#23000
arr = np.arange(6).reshape(3, 2)
df = DataFrame(arr, columns=[True, False], index=["A", "B", "C"])

rowlike = arr[[1], :]  # shape --> (1, ncols)
assert rowlike.shape == (1, df.shape[1])

expected = DataFrame(
    [[2, 4], [4, 6], [6, 8]],
    columns=df.columns,
    index=df.index,
    # specify dtype explicitly to avoid failing
    # on 32bit builds
    dtype=arr.dtype,
)
result = df + rowlike
tm.assert_frame_equal(result, expected)
result = rowlike + df
tm.assert_frame_equal(result, expected)
