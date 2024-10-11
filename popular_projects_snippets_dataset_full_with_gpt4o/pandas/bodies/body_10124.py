# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
with pytest.raises(ValueError, match="engine must be either 'numba' or 'cython'"):
    Series(range(1)).rolling(1).apply(lambda x: x, engine="foo")
