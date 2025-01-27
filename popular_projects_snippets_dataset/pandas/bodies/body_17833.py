# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_frame_equal.py
"""
    Check that two DataFrame equal.

    This check is performed commutatively.

    Parameters
    ----------
    a : DataFrame
        The first DataFrame to compare.
    b : DataFrame
        The second DataFrame to compare.
    kwargs : dict
        The arguments passed to `tm.assert_frame_equal`.
    """
tm.assert_frame_equal(a, b, **kwargs)
tm.assert_frame_equal(b, a, **kwargs)
