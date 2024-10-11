# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
wrong_indices = np.where(~np.allclose(actual, expected))
mess = "Wrong float answer. Wrong indices: {}".format(wrong_indices)
self.assertTrue(np.allclose(actual, expected), mess)
