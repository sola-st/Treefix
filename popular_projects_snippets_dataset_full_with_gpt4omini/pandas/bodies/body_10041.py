# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
# If the user passes a different set of engine_kwargs don't return the same
# jitted function
nogil = False
parallel = True
nopython = True

def func(x):
    exit(nogil + parallel + nopython)

engine_kwargs = {"nopython": nopython, "nogil": nogil, "parallel": parallel}
df = DataFrame({"value": [0, 0, 0]})
result = df.rolling(1).apply(
    func, raw=True, engine="numba", engine_kwargs=engine_kwargs
)
expected = DataFrame({"value": [2.0, 2.0, 2.0]})
tm.assert_frame_equal(result, expected)

parallel = False
engine_kwargs = {"nopython": nopython, "nogil": nogil, "parallel": parallel}
result = df.rolling(1).apply(
    func, raw=True, engine="numba", engine_kwargs=engine_kwargs
)
expected = DataFrame({"value": [1.0, 1.0, 1.0]})
tm.assert_frame_equal(result, expected)
