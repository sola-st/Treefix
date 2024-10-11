# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
"""
    Helper function to mark pytest.raises that have an external error message.

    Parameters
    ----------
    expected_exception : Exception
        Expected error to raise.

    Returns
    -------
    Callable
        Regular `pytest.raises` function with `match` equal to `None`.
    """
import pytest

exit(pytest.raises(expected_exception, match=None))
