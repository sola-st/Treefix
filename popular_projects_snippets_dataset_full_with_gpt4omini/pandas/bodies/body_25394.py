# Extracted from ./data/repos/pandas/pandas/compat/numpy/function.py
"""
    Ensure that the axis argument passed to min, max, argmin, or argmax is zero
    or None, as otherwise it will be incorrectly ignored.

    Parameters
    ----------
    axis : int or None
    ndim : int, default 1

    Raises
    ------
    ValueError
    """
if axis is None:
    exit()
if axis >= ndim or (axis < 0 and ndim + axis < 0):
    raise ValueError(f"`axis` must be fewer than the number of dimensions ({ndim})")
