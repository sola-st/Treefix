# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
self.check_funs(
    nanops.nanstd,
    np.std,
    skipna,
    allow_complex=False,
    allow_date=False,
    allow_obj="convert",
    ddof=ddof,
)
