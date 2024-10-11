# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
shape = [100, 100]
expect_mean = 0.
expect_var = 1. / shape[0]
init = init_ops_v2.VarianceScaling(distribution="uniform")

with test_util.use_gpu():
    x = self.evaluate(init(shape))

self.assertNear(np.mean(x), expect_mean, err=1e-2)
self.assertNear(np.var(x), expect_var, err=1e-2)
