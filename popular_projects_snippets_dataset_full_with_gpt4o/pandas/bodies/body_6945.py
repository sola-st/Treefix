# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_engines.py
# unique
arr = np.array(self.values, dtype=self.dtype)
engine = self.engine_type(arr)
assert engine.get_loc("b") == 1

# monotonic
num = 1000
arr = np.array(["a"] * num + ["b"] * num + ["c"] * num, dtype=self.dtype)
engine = self.engine_type(arr)
assert engine.get_loc("b") == slice(1000, 2000)

# not monotonic
arr = np.array(self.values * num, dtype=self.dtype)
engine = self.engine_type(arr)
expected = np.array([False, True, False] * num, dtype=bool)
result = engine.get_loc("b")
assert (result == expected).all()
