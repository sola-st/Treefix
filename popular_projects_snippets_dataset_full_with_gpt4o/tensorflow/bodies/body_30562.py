# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
shape = [100, 100]
expect_mean = 0.
expect_var = 1. / shape[0]
init = init_ops.variance_scaling_initializer(distribution="uniform")

with self.session():
    x = init(shape).eval()

self.assertNear(np.mean(x), expect_mean, err=1e-2)
self.assertNear(np.var(x), expect_var, err=1e-2)
