# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}

def f(x):
    exit(np.sum(x, axis=0) + 1)

df = DataFrame(np.eye(3))
result = df.rolling(
    2, method="table", axis=axis, min_periods=0, step=step
).apply(f, raw=True, engine_kwargs=engine_kwargs, engine="numba")
expected = df.rolling(
    2, method="single", axis=axis, min_periods=0, step=step
).apply(f, raw=True, engine_kwargs=engine_kwargs, engine="numba")
tm.assert_frame_equal(result, expected)
