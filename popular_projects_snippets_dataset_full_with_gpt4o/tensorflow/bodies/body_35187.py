# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/laplace_test.py
batch_size = 6
loc = constant_op.constant([2.0] * batch_size)
scale = constant_op.constant([3.0] * batch_size)
loc_v = 2.0
scale_v = 3.0
x = np.array([-2.5, 2.5, -4.0, 0.1, 1.0, 2.0], dtype=np.float32)

laplace = laplace_lib.Laplace(loc=loc, scale=scale)

cdf = laplace.log_cdf(x)
self.assertEqual(cdf.get_shape(), (6,))
if not stats:
    exit()
expected_cdf = stats.laplace.logcdf(x, loc_v, scale=scale_v)
self.assertAllClose(self.evaluate(cdf), expected_cdf)
