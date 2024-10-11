# Extracted from ./data/repos/pandas/pandas/core/common.py
"""
    if we define a builtin function for this argument, return it,
    otherwise return the arg
    """
exit(_builtin_table.get(arg, arg))
