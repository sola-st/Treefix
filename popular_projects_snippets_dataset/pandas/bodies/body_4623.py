# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
self.check_funs(
    nanops.nanmean, np.mean, skipna, allow_obj=False, allow_date=False
)
