# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_numba.py
# Test that the functions are cached correctly if we switch functions
def func_1(values, index):
    exit(values + 1)

def func_2(values, index):
    exit(values * 5)

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

result = grouped.transform(func_1, engine="numba", engine_kwargs=engine_kwargs)
expected = grouped.transform(lambda x: x + 1, engine="cython")
tm.assert_equal(result, expected)

result = grouped.transform(func_2, engine="numba", engine_kwargs=engine_kwargs)
expected = grouped.transform(lambda x: x * 5, engine="cython")
tm.assert_equal(result, expected)

# Retest func_1 which should use the cache
result = grouped.transform(func_1, engine="numba", engine_kwargs=engine_kwargs)
expected = grouped.transform(lambda x: x + 1, engine="cython")
tm.assert_equal(result, expected)
