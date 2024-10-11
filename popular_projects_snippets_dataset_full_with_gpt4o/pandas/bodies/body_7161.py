# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py

# these don't auto convert
self.check_coerce(
    float_index, Index((np.arange(5) * 2.5), dtype=object), is_float_index=False
)
self.check_coerce(
    mixed_index, Index([1.5, 2, 3, 4, 5], dtype=object), is_float_index=False
)
