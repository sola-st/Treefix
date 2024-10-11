# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
res = func(value, axis)
nans = np.min(value, axis)
nullnan = isna(nans)
if res.ndim:
    res[nullnan] = -1
elif (
    hasattr(nullnan, "all")
    and nullnan.all()
    or not hasattr(nullnan, "all")
    and nullnan
):
    res = -1
exit(res)
