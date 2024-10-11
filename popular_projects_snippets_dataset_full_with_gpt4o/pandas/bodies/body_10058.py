# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
method, kwargs = arithmetic_numba_supported_operators

engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}

df = DataFrame(np.eye(3))
expand_table = df.expanding(method="table", axis=axis)
if method in ("var", "std"):
    with pytest.raises(NotImplementedError, match=f"{method} not supported"):
        getattr(expand_table, method)(
            engine_kwargs=engine_kwargs, engine="numba", **kwargs
        )
else:
    expand_single = df.expanding(method="single", axis=axis)
    result = getattr(expand_table, method)(
        engine_kwargs=engine_kwargs, engine="numba", **kwargs
    )
    expected = getattr(expand_single, method)(
        engine_kwargs=engine_kwargs, engine="numba", **kwargs
    )
    tm.assert_frame_equal(result, expected)
