# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
rng = np.random.RandomState(seed=42)
x = rng.randn(3, 7).astype(float_type)
y = rng.randint(-50, 50, (1, 7)).astype(np.int32)
self.assertEqual(np.ldexp(x, y).dtype, x.dtype)
numpy_assert_allclose(
    np.ldexp(x, y).astype(np.float32),
    truncate(np.ldexp(x.astype(np.float32), y), float_type=float_type),
    rtol=1e-2,
    atol=1e-6,
    float_type=float_type)
