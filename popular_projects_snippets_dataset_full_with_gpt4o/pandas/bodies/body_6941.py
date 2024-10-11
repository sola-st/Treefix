# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_engines.py
engine_type, dtype = numeric_indexing_engine_type_and_dtype

# unique
arr = np.array([1, 3, 2], dtype=dtype)
engine = engine_type(arr)
assert engine.is_unique is True

# not unique
arr = np.array([1, 2, 1], dtype=dtype)
engine = engine_type(arr)
assert engine.is_unique is False
