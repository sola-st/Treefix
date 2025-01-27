# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
is_finite = np.isfinite(x)
all_true = np.ones_like(is_finite, dtype=np.bool_)
self.assertAllEqual(all_true, is_finite)
