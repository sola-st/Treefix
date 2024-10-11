# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py

method, kwargs = arithmetic_numba_supported_operators

engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}

roll = data.rolling(3, step=step)
result = getattr(roll, method)(
    engine="numba", engine_kwargs=engine_kwargs, **kwargs
)
expected = getattr(roll, method)(engine="cython", **kwargs)
tm.assert_equal(result, expected)
