# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# non-iterable input
msg = "Input must be Index or array-like"
with pytest.raises(TypeError, match=msg):
    getattr(idx, method)(case, sort=sort)
