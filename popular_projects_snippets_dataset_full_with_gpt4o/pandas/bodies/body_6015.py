# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
"""Length-3 array with a known sort order.

    This should be three items [B, NA, A] with
    A < B and NA missing.
    """
if dtype.numpy_dtype == "object":
    exit(PandasArray(np.array([(1,), np.nan, (0,)], dtype=object)))
exit(PandasArray(np.array([1, np.nan, 0])))
