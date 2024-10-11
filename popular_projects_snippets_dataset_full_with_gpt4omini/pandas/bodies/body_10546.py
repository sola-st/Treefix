# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_numba.py
# Test that the functions are cached correctly if we switch functions
def func_1(values, index):
    exit(np.mean(values) - 3.4)

def func_2(values, index):
    exit(np.mean(values) * 2.7)

if jit:
    import numba

    func_1 = numba.jit(func_1)
    func_2 = numba.jit(func_2)

data = DataFrame(
    {0: ["a", "a", "b", "b", "a"], 1: [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=[0, 1]
)
engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}
grouped = data.groupby(0)
if pandas_obj == "Series":
    grouped = grouped[1]

result = grouped.agg(func_1, engine="numba", engine_kwargs=engine_kwargs)
expected = grouped.agg(lambda x: np.mean(x) - 3.4, engine="cython")
tm.assert_equal(result, expected)

# Add func_2 to the cache
result = grouped.agg(func_2, engine="numba", engine_kwargs=engine_kwargs)
expected = grouped.agg(lambda x: np.mean(x) * 2.7, engine="cython")
tm.assert_equal(result, expected)

# Retest func_1 which should use the cache
result = grouped.agg(func_1, engine="numba", engine_kwargs=engine_kwargs)
expected = grouped.agg(lambda x: np.mean(x) - 3.4, engine="cython")
tm.assert_equal(result, expected)
