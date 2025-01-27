# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
a = np.array([1., 2, 3])
b = np.array([2., 4, 1.2])
dist = beta_lib.Beta(a, b, allow_nan_stats=False)
with self.assertRaisesOpError("Condition x < y.*"):
    self.evaluate(dist.mode())

a = np.array([2., 2, 3])
b = np.array([1., 4, 1.2])
dist = beta_lib.Beta(a, b, allow_nan_stats=False)
with self.assertRaisesOpError("Condition x < y.*"):
    self.evaluate(dist.mode())
