# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
with pytest.raises(NumbaUtilError, match="numba does not support kwargs with"):
    Series(range(1)).rolling(1).apply(
        lambda x: x, kwargs={"a": 1}, engine="numba", raw=True
    )
