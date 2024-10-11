# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
msg = "must be convertible to a list-of-tuples"
with pytest.raises(TypeError, match=msg):
    hash_tuples(val)
