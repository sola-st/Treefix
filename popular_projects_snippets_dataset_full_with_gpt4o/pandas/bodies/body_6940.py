# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_engines.py
engine_type, dtype = numeric_indexing_engine_type_and_dtype
num = 1000
arr = np.array([1] * num + [2] * num + [3] * num, dtype=dtype)

# monotonic increasing
engine = engine_type(arr)
assert engine.is_monotonic_increasing is True
assert engine.is_monotonic_decreasing is False

# monotonic decreasing
engine = engine_type(arr[::-1])
assert engine.is_monotonic_increasing is False
assert engine.is_monotonic_decreasing is True

# neither monotonic increasing or decreasing
arr = np.array([1] * num + [2] * num + [1] * num, dtype=dtype)
engine = engine_type(arr[::-1])
assert engine.is_monotonic_increasing is False
assert engine.is_monotonic_decreasing is False
