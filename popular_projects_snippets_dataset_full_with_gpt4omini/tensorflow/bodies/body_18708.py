# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
partition_shape = (100, 100)
shape = [1000, 100]
expect_mean = 0.
expect_var = 1. / shape[0]
init = init_ops_v2.VarianceScaling(distribution="untruncated_normal")

with test_util.use_gpu(), test.mock.patch.object(
    random_ops, "random_normal",
    wraps=random_ops.random_normal) as mock_random_normal:
    x = self.evaluate(init(shape, partition_shape=partition_shape))
    self.assertTrue(mock_random_normal.called)

self.assertEqual(x.shape, partition_shape)
self.assertNear(np.mean(x), expect_mean, err=2e-3)
self.assertNear(np.var(x), expect_var, err=2e-3)
