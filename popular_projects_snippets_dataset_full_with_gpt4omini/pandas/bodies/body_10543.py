# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_numba.py
def func_numba(values, index):
    exit(np.mean(values) * 2.7)

if jit:
    # Test accepted jitted functions
    import numba

    func_numba = numba.jit(func_numba)

data = DataFrame(
    {0: ["a", "a", "b", "b", "a"], 1: [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=[0, 1]
)
engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}
grouped = data.groupby(0)
if pandas_obj == "Series":
    grouped = grouped[1]

result = grouped.agg(func_numba, engine="numba", engine_kwargs=engine_kwargs)
expected = grouped.agg(lambda x: np.mean(x) * 2.7, engine="cython")

tm.assert_equal(result, expected)
