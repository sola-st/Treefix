# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_numba.py
func, kwargs = numba_supported_reductions
ser = Series(range(3), index=[1, 2, 1], name="foo")
engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}
gb = ser.groupby(level=0, sort=sort)
result = getattr(gb, func)(
    engine="numba", engine_kwargs=engine_kwargs, **kwargs
)
expected = getattr(gb, func)(**kwargs)
# check_dtype can be removed if GH 44952 is addressed
check_dtype = func not in ("sum", "min", "max")
tm.assert_series_equal(result, expected, check_dtype=check_dtype)
