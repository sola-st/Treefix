# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_numba.py
func, kwargs = numba_supported_reductions
df = DataFrame({"a": [3, 2, 3, 2], "b": range(4), "c": range(1, 5)})
engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}
gb = df.groupby("a", sort=sort)["c"]
result = getattr(gb, func)(
    engine="numba", engine_kwargs=engine_kwargs, **kwargs
)
expected = getattr(gb, func)(**kwargs)
# check_dtype can be removed if GH 44952 is addressed
check_dtype = func not in ("sum", "min", "max")
tm.assert_series_equal(result, expected, check_dtype=check_dtype)
