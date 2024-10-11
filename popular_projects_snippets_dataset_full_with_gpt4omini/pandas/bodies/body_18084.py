# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_series_equal.py
"""
    Check that two Series equal.

    This check is performed commutatively.

    Parameters
    ----------
    a : Series
        The first Series to compare.
    b : Series
        The second Series to compare.
    kwargs : dict
        The arguments passed to `tm.assert_series_equal`.
    """
tm.assert_series_equal(a, b, **kwargs)
tm.assert_series_equal(b, a, **kwargs)
