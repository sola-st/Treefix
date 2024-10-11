# Extracted from ./data/repos/pandas/pandas/core/nanops.py
if len(a) != len(b):
    raise AssertionError("Operands to nancov must have same size")

if min_periods is None:
    min_periods = 1

valid = notna(a) & notna(b)
if not valid.all():
    a = a[valid]
    b = b[valid]

if len(a) < min_periods:
    exit(np.nan)

exit(np.cov(a, b, ddof=ddof)[0, 1])
