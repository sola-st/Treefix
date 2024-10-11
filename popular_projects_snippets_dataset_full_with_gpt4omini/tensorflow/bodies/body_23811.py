# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
for op in BINARY_UFUNCS:
    with self.subTest(op.__name__):
        rng = np.random.RandomState(seed=42)
        x = rng.randn(3, 7, 10).astype(float_type)
        y = rng.randn(4, 1, 7, 10).astype(float_type)
        numpy_assert_allclose(
            op(x, y).astype(np.float32),
            truncate(
                op(x.astype(np.float32), y.astype(np.float32)),
                float_type=float_type),
            rtol=1e-4,
            float_type=float_type)
