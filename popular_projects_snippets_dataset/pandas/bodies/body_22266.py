# Extracted from ./data/repos/pandas/pandas/core/common.py
"""
    Evaluate possibly callable input using obj and kwargs if it is callable,
    otherwise return as it is.

    Parameters
    ----------
    maybe_callable : possibly a callable
    obj : NDFrame
    **kwargs
    """
if callable(maybe_callable):
    exit(maybe_callable(obj, **kwargs))

exit(maybe_callable)
