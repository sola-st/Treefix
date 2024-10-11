# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
self.check_fun(testfunc, targfunc, "arr_float", skipna, **kwargs)
self.check_fun(testfunc, targfunc, "arr_float_nan", skipna, **kwargs)
self.check_fun(testfunc, targfunc, "arr_int", skipna, **kwargs)
self.check_fun(testfunc, targfunc, "arr_bool", skipna, **kwargs)
objs = [
    self.arr_float.astype("O"),
    self.arr_int.astype("O"),
    self.arr_bool.astype("O"),
]

if allow_all_nan:
    self.check_fun(testfunc, targfunc, "arr_nan", skipna, **kwargs)

if allow_complex:
    self.check_fun(testfunc, targfunc, "arr_complex", skipna, **kwargs)
    self.check_fun(testfunc, targfunc, "arr_complex_nan", skipna, **kwargs)
    if allow_all_nan:
        self.check_fun(testfunc, targfunc, "arr_nan_nanj", skipna, **kwargs)
    objs += [self.arr_complex.astype("O")]

if allow_date:
    targfunc(self.arr_date)
    self.check_fun(testfunc, targfunc, "arr_date", skipna, **kwargs)
    objs += [self.arr_date.astype("O")]

if allow_tdelta:
    try:
        targfunc(self.arr_tdelta)
    except TypeError:
        pass
    else:
        self.check_fun(testfunc, targfunc, "arr_tdelta", skipna, **kwargs)
        objs += [self.arr_tdelta.astype("O")]

if allow_obj:
    self.arr_obj = np.vstack(objs)
    # some nanops handle object dtypes better than their numpy
    # counterparts, so the numpy functions need to be given something
    # else
    if allow_obj == "convert":
        targfunc = partial(
            self._badobj_wrap, func=targfunc, allow_complex=allow_complex
        )
    self.check_fun(testfunc, targfunc, "arr_obj", skipna, **kwargs)
