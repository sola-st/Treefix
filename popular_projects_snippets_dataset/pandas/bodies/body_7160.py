# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py

self.check_coerce(mixed_index, Index([1.5, 2, 3, 4, 5]))
self.check_coerce(float_index, Index(np.arange(5) * 2.5))

result = Index(np.array(np.arange(5) * 2.5, dtype=object))
assert result.dtype == object  # as of 2.0 to match Series
self.check_coerce(float_index, result.astype("float64"))
