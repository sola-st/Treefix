# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
with warnings.catch_warnings(record=True):
    warnings.simplefilter("ignore", RuntimeWarning)
    func = partial(self._argminmax_wrap, func=np.argmax)
    self.check_funs(nanops.nanargmax, func, skipna, allow_obj=False)
