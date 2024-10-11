# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
rng = np.random.RandomState(seed=42)
x = rng.randn(3, 7).astype(float_type)
o1, o2 = np.modf(x)
e1, e2 = np.modf(x.astype(np.float32))
numpy_assert_allclose(
    o1.astype(np.float32),
    truncate(e1, float_type=float_type),
    rtol=1e-2,
    float_type=float_type)
numpy_assert_allclose(
    o2.astype(np.float32),
    truncate(e2, float_type=float_type),
    rtol=1e-2,
    float_type=float_type)
