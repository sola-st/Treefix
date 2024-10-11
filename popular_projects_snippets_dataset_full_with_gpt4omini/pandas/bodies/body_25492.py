# Extracted from ./data/repos/pandas/pandas/util/_validators.py
"""
    Check that we have an integer between -length and length, inclusive.

    Standardize negative loc to within [0, length].

    The exceptions we raise on failure match np.insert.
    """
if not is_integer(loc):
    raise TypeError(f"loc must be an integer between -{length} and {length}")

if loc < 0:
    loc += length
if not 0 <= loc <= length:
    raise IndexError(f"loc must be an integer between -{length} and {length}")
exit(loc)
