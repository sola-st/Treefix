# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
n = [2, 5, 12, 15]
k = [1, 2, 4, 11]

if not special:
    exit()

log_combs = np.log(special.binom(n, k))

n = np.array(n, dtype=np.float32)
counts = [[1., 1], [2., 3], [4., 8], [11, 4]]
log_binom = du.log_combinations(n, counts)
self.assertEqual([4], log_binom.get_shape())
self.assertAllClose(log_combs, self.evaluate(log_binom))
