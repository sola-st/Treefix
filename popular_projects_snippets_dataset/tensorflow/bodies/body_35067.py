# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x = array_ops.zeros((2, 3, 4))
rank = du.prefer_static_rank(x)
self.assertIsInstance(rank, np.ndarray)
self.assertEqual(3, rank)
