# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_numba.py
def func(values, index):
    exit(values + 1)

if jit:
    # Test accepted jitted functions
    import numba

    func = numba.jit(func)

data = DataFrame(
    {0: ["a", "a", "b", "b", "a"], 1: [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=[0, 1]
)
engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}
grouped = data.groupby(0)
if pandas_obj == "Series":
    grouped = grouped[1]

result = grouped.transform(func, engine="numba", engine_kwargs=engine_kwargs)
expected = grouped.transform(lambda x: x + 1, engine="cython")

tm.assert_equal(result, expected)
