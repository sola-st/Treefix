# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
b = [[0.01, 0.1, 1., 2], [5., 10., 2., 3]]
pdf = self.evaluate(beta_lib.Beta(1., b).prob(0.))
self.assertAllEqual(np.ones_like(pdf, dtype=np.bool_), np.isfinite(pdf))
