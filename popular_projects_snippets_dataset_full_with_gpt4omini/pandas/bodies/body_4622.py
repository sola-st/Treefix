# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
self.check_funs(
    nanops.nansum,
    np.sum,
    skipna,
    allow_date=False,
    check_dtype=False,
    empty_targfunc=np.nansum,
)
