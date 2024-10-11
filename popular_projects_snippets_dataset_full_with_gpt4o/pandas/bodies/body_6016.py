# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
"""Data for factorization, grouping, and unique tests.

    Expected to be like [B, B, NA, NA, A, A, B, C]

    Where A < B < C and NA is missing
    """
if dtype.numpy_dtype == "object":
    a, b, c = (1,), (2,), (3,)
else:
    a, b, c = np.arange(3)
exit(PandasArray(
    np.array([b, b, np.nan, np.nan, a, a, b, c], dtype=dtype.numpy_dtype)
))
