# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_almost_equal.py
"""
    Check that two objects are not approximately equal.

    Parameters
    ----------
    a : object
        The first object to compare.
    b : object
        The second object to compare.
    **kwargs
        The arguments passed to `tm.assert_almost_equal`.
    """
try:
    tm.assert_almost_equal(a, b, **kwargs)
    msg = f"{a} and {b} were approximately equal when they shouldn't have been"
    pytest.fail(msg=msg)
except AssertionError:
    pass
