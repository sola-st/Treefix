# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_numba.py
def numba_func(values, index):
    exit(1)

df = DataFrame([{"A": 1, "B": 2, "C": 3}]).set_index(["A", "B"])
engine_kwargs = {"nopython": nopython, "nogil": nogil, "parallel": parallel}
result = df.groupby("A").transform(
    numba_func, engine="numba", engine_kwargs=engine_kwargs
)
expected = DataFrame([{"A": 1, "B": 2, "C": 1.0}]).set_index(["A", "B"])
tm.assert_frame_equal(result, expected)
