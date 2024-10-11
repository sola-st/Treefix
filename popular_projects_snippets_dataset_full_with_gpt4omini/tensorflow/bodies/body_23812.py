# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
for op in BINARY_PREDICATE_UFUNCS:
    with self.subTest(op.__name__):
        rng = np.random.RandomState(seed=42)
        x = rng.randn(3, 7).astype(float_type)
        y = rng.randn(4, 1, 7).astype(float_type)
        np.testing.assert_equal(
            op(x, y), op(x.astype(np.float32), y.astype(np.float32)))
