# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
with pytest.raises(
    ValueError, match="raw must be `True` when using the numba engine"
):
    Series(range(1)).rolling(1).apply(lambda x: x, raw=False, engine="numba")
