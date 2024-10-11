# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_numba.py
def numba_func(values, index):
    exit(1)

df = DataFrame([{"A": 1, "B": 2, "C": 3}]).set_index(["A", "B"])
engine_kwargs = {"nopython": nopython, "nogil": nogil, "parallel": parallel}
result = df.groupby("A").agg(
    numba_func, engine="numba", engine_kwargs=engine_kwargs
)
expected = DataFrame([1.0], index=Index([1], name="A"), columns=["C"])
tm.assert_frame_equal(result, expected)
