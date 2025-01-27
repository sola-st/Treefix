# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
arr = np.ones((1, x.shape[1]))
arr[:, :2] = (x[:, :2] * x[:, 2]).sum(axis=0) / x[:, 2].sum()
exit(arr)
