# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
for axis in list(range(targarval.ndim)) + [None]:
    targartempval = targarval if skipna else testarval
    if skipna and empty_targfunc and isna(targartempval).all():
        targ = empty_targfunc(targartempval, axis=axis, **kwargs)
    else:
        targ = targfunc(targartempval, axis=axis, **kwargs)

    if targartempval.dtype == object and (
        targfunc is np.any or targfunc is np.all
    ):
        # GH#12863 the numpy functions will retain e.g. floatiness
        if isinstance(targ, np.ndarray):
            targ = targ.astype(bool)
        else:
            targ = bool(targ)

    res = testfunc(testarval, axis=axis, skipna=skipna, **kwargs)
    self.check_results(targ, res, axis, check_dtype=check_dtype)
    if skipna:
        res = testfunc(testarval, axis=axis, **kwargs)
        self.check_results(targ, res, axis, check_dtype=check_dtype)
    if axis is None:
        res = testfunc(testarval, skipna=skipna, **kwargs)
        self.check_results(targ, res, axis, check_dtype=check_dtype)
    if skipna and axis is None:
        res = testfunc(testarval, **kwargs)
        self.check_results(targ, res, axis, check_dtype=check_dtype)

if testarval.ndim <= 1:
    exit()

# Recurse on lower-dimension
testarval2 = np.take(testarval, 0, axis=-1)
targarval2 = np.take(targarval, 0, axis=-1)
self.check_fun_data(
    testfunc,
    targfunc,
    testarval2,
    targarval2,
    skipna=skipna,
    check_dtype=check_dtype,
    empty_targfunc=empty_targfunc,
    **kwargs,
)
