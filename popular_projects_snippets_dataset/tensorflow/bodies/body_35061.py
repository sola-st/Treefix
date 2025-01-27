# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
# Shape [2, 2]
n = [[2, 5], [12, 15]]

n = np.array(n, dtype=np.float32)
# Shape [2, 2, 4]
counts = [[[1., 1, 0, 0], [2., 2, 1, 0]], [[4., 4, 1, 3], [10, 1, 1, 4]]]
log_binom = du.log_combinations(n, counts)
self.assertEqual([2, 2], log_binom.get_shape())
