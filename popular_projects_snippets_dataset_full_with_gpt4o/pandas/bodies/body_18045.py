# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
# This only matters for object dtypes.
msg = "key should be a 16-byte string encoded"

with pytest.raises(ValueError, match=msg):
    hash_pandas_object(Series(list("abc")), hash_key="foo")
