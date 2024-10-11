# Extracted from ./data/repos/pandas/pandas/core/computation/eval.py
"""
    Make sure an expression is not an empty string

    Parameters
    ----------
    expr : object
        An object that can be converted to a string

    Raises
    ------
    ValueError
      * If expr is an empty string
    """
if not expr:
    raise ValueError("expr cannot be an empty string")
