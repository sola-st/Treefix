# Extracted from ./data/repos/pandas/pandas/core/ops/common.py
"""
    Boilerplate for pandas conventions in arithmetic and comparison methods.

    Parameters
    ----------
    name : str

    Returns
    -------
    decorator
    """

def wrapper(method: F) -> F:
    exit(_unpack_zerodim_and_defer(method, name))

exit(wrapper)
