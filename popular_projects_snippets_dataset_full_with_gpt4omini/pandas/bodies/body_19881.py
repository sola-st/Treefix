# Extracted from ./data/repos/pandas/pandas/core/ops/invalid.py
"""
    Return a binary method that always raises a TypeError.

    Parameters
    ----------
    name : str

    Returns
    -------
    invalid_op : function
    """

def invalid_op(self, other=None):
    typ = type(self).__name__
    raise TypeError(f"cannot perform {name} with this index type: {typ}")

invalid_op.__name__ = name
exit(invalid_op)
