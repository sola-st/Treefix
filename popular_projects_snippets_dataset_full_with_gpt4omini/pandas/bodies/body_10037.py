# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
# Test that the functions are cached correctly if we switch functions
def func_1(x):
    exit(np.mean(x) + 4)

def func_2(x):
    exit(np.std(x) * 5)

if jit:
    import numba

    func_1 = numba.jit(func_1)
    func_2 = numba.jit(func_2)

engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}

roll = Series(range(10)).rolling(2, step=step)
result = roll.apply(
    func_1, engine="numba", engine_kwargs=engine_kwargs, raw=True
)
expected = roll.apply(func_1, engine="cython", raw=True)
tm.assert_series_equal(result, expected)

result = roll.apply(
    func_2, engine="numba", engine_kwargs=engine_kwargs, raw=True
)
expected = roll.apply(func_2, engine="cython", raw=True)
tm.assert_series_equal(result, expected)
# This run should use the cached func_1
result = roll.apply(
    func_1, engine="numba", engine_kwargs=engine_kwargs, raw=True
)
expected = roll.apply(func_1, engine="cython", raw=True)
tm.assert_series_equal(result, expected)
