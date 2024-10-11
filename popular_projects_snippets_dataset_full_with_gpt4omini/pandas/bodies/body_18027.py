# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
msg = "must pass a ndarray-like"
with pytest.raises(TypeError, match=msg):
    hash_array(val)
