# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_numba.py
def numba_func(values, index):
    exit(1)

df = DataFrame([{"A": 1, "B": 2, "C": 3}]).set_index(["A", "B"])
engine_kwargs = {"nopython": nopython, "nogil": nogil, "parallel": parallel}
with pytest.raises(NotImplementedError, match="More than 1 grouping labels"):
    df.groupby(["A", "B"]).agg(
        numba_func, engine="numba", engine_kwargs=engine_kwargs
    )
