# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#23000
arr = np.arange(6).reshape(3, 2)
df = DataFrame(arr, columns=[True, False], index=["A", "B", "C"])

collike = arr[:, [1]]  # shape --> (nrows, 1)
assert collike.shape == (df.shape[0], 1)

expected = DataFrame(
    [[1, 2], [5, 6], [9, 10]],
    columns=df.columns,
    index=df.index,
    # specify dtype explicitly to avoid failing
    # on 32bit builds
    dtype=arr.dtype,
)
result = df + collike
tm.assert_frame_equal(result, expected)
result = collike + df
tm.assert_frame_equal(result, expected)
