# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}

df = DataFrame(data)

result = getattr(df.ewm(com=1, method="table", axis=axis), method)(
    engine_kwargs=engine_kwargs, engine="numba"
)
expected = getattr(df.ewm(com=1, method="single", axis=axis), method)(
    engine_kwargs=engine_kwargs, engine="numba"
)
tm.assert_frame_equal(result, expected)
