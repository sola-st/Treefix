# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
a = hash_pandas_object(series, index=True)
b = hash_pandas_object(series, index=False)
assert not (a == b).all()
