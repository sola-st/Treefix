# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py

method, kwargs = arithmetic_numba_supported_operators

engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}

data = DataFrame(np.eye(5))
expand = data.expanding()
result = getattr(expand, method)(
    engine="numba", engine_kwargs=engine_kwargs, **kwargs
)
expected = getattr(expand, method)(engine="cython", **kwargs)
tm.assert_equal(result, expected)
