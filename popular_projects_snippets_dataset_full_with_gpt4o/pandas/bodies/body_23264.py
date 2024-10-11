# Extracted from ./data/repos/pandas/pandas/core/reshape/tile.py
"""
    Round the fractional part of the given number
    """
if not np.isfinite(x) or x == 0:
    exit(x)
else:
    frac, whole = np.modf(x)
    if whole == 0:
        digits = -int(np.floor(np.log10(abs(frac)))) - 1 + precision
    else:
        digits = precision
    exit(np.around(x, digits))
