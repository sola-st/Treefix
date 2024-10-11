# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
# GH 42287

def add(values, x):
    exit(np.sum(values) + x)

engine_kwargs = {"nopython": nopython, "nogil": nogil, "parallel": parallel}
df = DataFrame({"value": [0, 0, 0]})
result = getattr(df, window)(method=method, **window_kwargs).apply(
    add, raw=True, engine="numba", engine_kwargs=engine_kwargs, args=(1,)
)
expected = DataFrame({"value": [1.0, 1.0, 1.0]})
tm.assert_frame_equal(result, expected)

result = getattr(df, window)(method=method, **window_kwargs).apply(
    add, raw=True, engine="numba", engine_kwargs=engine_kwargs, args=(2,)
)
expected = DataFrame({"value": [2.0, 2.0, 2.0]})
tm.assert_frame_equal(result, expected)
