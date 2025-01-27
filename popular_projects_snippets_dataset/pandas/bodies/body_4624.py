# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
with warnings.catch_warnings(record=True):
    warnings.simplefilter("ignore", RuntimeWarning)
    self.check_funs(
        nanops.nanmedian,
        np.median,
        skipna,
        allow_complex=False,
        allow_date=False,
        allow_obj="convert",
    )
