# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
is_finite = np.isfinite(self.evaluate(tensor))
all_true = np.ones_like(is_finite, dtype=np.bool_)
self.assertAllEqual(all_true, is_finite)
