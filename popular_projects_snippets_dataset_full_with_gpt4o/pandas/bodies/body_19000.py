# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
"""
    Compute the vectorized membership of ``x not in y`` if possible,
    otherwise use Python.
    """
try:
    exit(~x.isin(y))
except AttributeError:
    if is_list_like(x):
        try:
            exit(~y.isin(x))
        except AttributeError:
            pass
    exit(x not in y)
