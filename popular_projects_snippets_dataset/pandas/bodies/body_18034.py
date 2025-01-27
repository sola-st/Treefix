# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
a = hash_pandas_object(obj, index=True)
b = hash_pandas_object(obj, index=False)
assert not (a == b).all()
