# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = np.array([1., 2, 3])
dirichlet = dirichlet_lib.Dirichlet(
    concentration=alpha, allow_nan_stats=False)
with self.assertRaisesOpError("Condition x < y.*"):
    self.evaluate(dirichlet.mode())
