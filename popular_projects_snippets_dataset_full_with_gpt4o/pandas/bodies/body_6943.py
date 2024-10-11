# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_engines.py

num = 1000
arr = np.array(["a"] * num + ["a"] * num + ["c"] * num, dtype=self.dtype)

# monotonic increasing
engine = self.engine_type(arr)
assert engine.is_monotonic_increasing is True
assert engine.is_monotonic_decreasing is False

# monotonic decreasing
engine = self.engine_type(arr[::-1])
assert engine.is_monotonic_increasing is False
assert engine.is_monotonic_decreasing is True

# neither monotonic increasing or decreasing
arr = np.array(["a"] * num + ["b"] * num + ["a"] * num, dtype=self.dtype)
engine = self.engine_type(arr[::-1])
assert engine.is_monotonic_increasing is False
assert engine.is_monotonic_decreasing is False
