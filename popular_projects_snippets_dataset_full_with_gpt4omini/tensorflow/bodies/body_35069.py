# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x = constant_op.constant(1.)
rank = du.prefer_static_rank(x)
self.assertIsInstance(rank, np.ndarray)
self.assertEqual(0, rank)
