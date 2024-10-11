# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_engines.py
engine_type, dtype = numeric_indexing_engine_type_and_dtype

# unique
arr = np.array([1, 2, 3], dtype=dtype)
engine = engine_type(arr)
assert engine.get_loc(2) == 1

# monotonic
num = 1000
arr = np.array([1] * num + [2] * num + [3] * num, dtype=dtype)
engine = engine_type(arr)
assert engine.get_loc(2) == slice(1000, 2000)

# not monotonic
arr = np.array([1, 2, 3] * num, dtype=dtype)
engine = engine_type(arr)
expected = np.array([False, True, False] * num, dtype=bool)
result = engine.get_loc(2)
assert (result == expected).all()
