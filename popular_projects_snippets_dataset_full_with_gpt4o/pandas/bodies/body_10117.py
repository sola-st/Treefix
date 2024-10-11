# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
with pytest.raises(ValueError, match="raw parameter must be `True` or `False`"):
    Series(range(3)).rolling(1).apply(len, raw=bad_raw)
