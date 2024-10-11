# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
with warnings.catch_warnings(record=True):
    warnings.simplefilter("ignore", RuntimeWarning)
    self.check_funs(nan_op, np_op, skipna, allow_obj=False)
