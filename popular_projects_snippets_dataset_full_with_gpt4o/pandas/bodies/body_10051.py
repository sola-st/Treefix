# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
method, kwargs = arithmetic_numba_supported_operators

engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}

df = DataFrame(np.eye(3))
roll_table = df.rolling(2, method="table", axis=axis, min_periods=0, step=step)
if method in ("var", "std"):
    with pytest.raises(NotImplementedError, match=f"{method} not supported"):
        getattr(roll_table, method)(
            engine_kwargs=engine_kwargs, engine="numba", **kwargs
        )
else:
    roll_single = df.rolling(
        2, method="single", axis=axis, min_periods=0, step=step
    )
    result = getattr(roll_table, method)(
        engine_kwargs=engine_kwargs, engine="numba", **kwargs
    )
    expected = getattr(roll_single, method)(
        engine_kwargs=engine_kwargs, engine="numba", **kwargs
    )
    tm.assert_frame_equal(result, expected)
