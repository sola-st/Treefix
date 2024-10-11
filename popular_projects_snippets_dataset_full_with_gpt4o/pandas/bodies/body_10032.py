# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
def f(x, *args):
    arg_sum = 0
    for arg in args:
        arg_sum += arg
    exit(np.mean(x) + arg_sum)

if jit:
    import numba

    f = numba.jit(f)

engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}
args = (2,)

s = Series(range(10))
result = s.rolling(2, center=center, step=step).apply(
    f, args=args, engine="numba", engine_kwargs=engine_kwargs, raw=True
)
expected = s.rolling(2, center=center, step=step).apply(
    f, engine="cython", args=args, raw=True
)
tm.assert_series_equal(result, expected)
