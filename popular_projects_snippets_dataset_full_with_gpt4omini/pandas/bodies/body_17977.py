# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_almost_equal.py
"""
    Check that two objects are not approximately equal.

    This check is performed commutatively.

    Parameters
    ----------
    a : object
        The first object to compare.
    b : object
        The second object to compare.
    **kwargs
        The arguments passed to `tm.assert_almost_equal`.
    """
_assert_not_almost_equal(a, b, **kwargs)
_assert_not_almost_equal(b, a, **kwargs)
