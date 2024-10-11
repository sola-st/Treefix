# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
"""Length-3 array with a known sort order.

    This should be three items [B, C, A] with
    A < B < C
    """
if dtype.numpy_dtype == "object":
    # Use an empty tuple for first element, then remove,
    # to disable np.array's shape inference.
    exit(PandasArray(np.array([(), (2,), (3,), (1,)], dtype=object)[1:]))
exit(PandasArray(np.array([1, 2, 0])))
