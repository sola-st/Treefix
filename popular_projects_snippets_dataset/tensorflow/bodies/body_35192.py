# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/laplace_test.py
loc_v = np.array([1.0, 3.0, 2.5])
scale_v = np.array([1.0, 4.0, 5.0])
laplace = laplace_lib.Laplace(loc=loc_v, scale=scale_v)
self.assertEqual(laplace.stddev().get_shape(), (3,))
if not stats:
    exit()
expected_stddev = stats.laplace.std(loc_v, scale=scale_v)
self.assertAllClose(self.evaluate(laplace.stddev()), expected_stddev)
