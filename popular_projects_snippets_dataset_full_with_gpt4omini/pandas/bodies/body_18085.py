# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_series_equal.py
"""
    Check that two Series are not equal.

    Parameters
    ----------
    a : Series
        The first Series to compare.
    b : Series
        The second Series to compare.
    kwargs : dict
        The arguments passed to `tm.assert_series_equal`.
    """
try:
    tm.assert_series_equal(a, b, **kwargs)
    msg = "The two Series were equal when they shouldn't have been"

    pytest.fail(msg=msg)
except AssertionError:
    pass
