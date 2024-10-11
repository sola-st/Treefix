# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_compat.py
msg = f"cannot perform {method}"

with pytest.raises(TypeError, match=msg):
    getattr(idx, method)()
