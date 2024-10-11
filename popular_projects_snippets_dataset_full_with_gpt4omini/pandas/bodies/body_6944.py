# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_engines.py
# unique
arr = np.array(self.values, dtype=self.dtype)
engine = self.engine_type(arr)
assert engine.is_unique is True

# not unique
arr = np.array(["a", "b", "a"], dtype=self.dtype)
engine = self.engine_type(arr)
assert engine.is_unique is False
