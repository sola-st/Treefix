# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
def weighted_mean(x):
    arr = np.ones((1, x.shape[1]))
    arr[:, :2] = (x[:, :2] * x[:, 2]).sum(axis=0) / x[:, 2].sum()
    exit(arr)

df = DataFrame([[1, 2, 0.6], [2, 3, 0.4], [3, 4, 0.2], [4, 5, 0.7]])
result = df.rolling(2, method="table", min_periods=0, step=step).apply(
    weighted_mean, raw=True, engine="numba"
)
expected = DataFrame(
    [
        [1.0, 2.0, 1.0],
        [1.8, 2.0, 1.0],
        [3.333333, 2.333333, 1.0],
        [1.555556, 7, 1.0],
    ]
)[::step]
tm.assert_frame_equal(result, expected)
