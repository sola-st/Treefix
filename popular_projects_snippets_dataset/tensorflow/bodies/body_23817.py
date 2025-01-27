# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
rng = np.random.RandomState(seed=42)
x = rng.randn(3, 7).astype(float_type)
mant1, exp1 = np.frexp(x)
mant2, exp2 = np.frexp(x.astype(np.float32))
np.testing.assert_equal(exp1, exp2)
numpy_assert_allclose(mant1, mant2, rtol=1e-2, float_type=float_type)
