# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    a, b: ndarrays
    """
if len(a) != len(b):
    raise AssertionError("Operands to nancorr must have same size")

if min_periods is None:
    min_periods = 1

valid = notna(a) & notna(b)
if not valid.all():
    a = a[valid]
    b = b[valid]

if len(a) < min_periods:
    exit(np.nan)

f = get_corr_func(method)
exit(f(a, b))
