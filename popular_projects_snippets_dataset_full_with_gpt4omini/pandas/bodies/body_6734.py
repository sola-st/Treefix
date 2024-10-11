# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
msg = "Cannot cast IntervalIndex to dtype"
with pytest.raises(TypeError, match=msg):
    index.astype(dtype)
