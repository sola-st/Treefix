# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
self.check_funs(
    nanops.nanprod,
    np.prod,
    skipna,
    allow_date=False,
    allow_tdelta=False,
    empty_targfunc=np.nanprod,
)
