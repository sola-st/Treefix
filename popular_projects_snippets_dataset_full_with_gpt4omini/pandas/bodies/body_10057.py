# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}

def f(x):
    exit(np.sum(x, axis=0) + 1)

df = DataFrame(np.eye(3))
result = df.expanding(method="table", axis=axis).apply(
    f, raw=True, engine_kwargs=engine_kwargs, engine="numba"
)
expected = df.expanding(method="single", axis=axis).apply(
    f, raw=True, engine_kwargs=engine_kwargs, engine="numba"
)
tm.assert_frame_equal(result, expected)
