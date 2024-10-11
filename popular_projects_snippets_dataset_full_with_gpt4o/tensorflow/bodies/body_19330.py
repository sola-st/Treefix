# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/matmul_benchmark.py
dtypes = [np.float32, np.float64]
for dtype in dtypes:
    for n, m, (transpose_a, transpose_b) in itertools.product(
        [512, 1024], [1, 8, 16, 128], [(False, False), (True, False),
                                       (False, True)]):
        k = n
        self.run_test_gpu(n, m, k, transpose_a, transpose_b, dtype, num_iters)

    for n, m, k, (transpose_a, transpose_b) in itertools.product(
        [200], [1, 8, 20], [10000], [(False, False), (True, False),
                                     (False, True)]):
        self.run_test_gpu(n, m, k, transpose_a, transpose_b, dtype, num_iters)

    for (n, m, k), (transpose_a, transpose_b) in itertools.product(
        [(200, 20, 20000), (1, 10000, 200)], [(False, False), (True, False),
                                              (False, True)]):
        self.run_test_gpu(n, m, k, transpose_a, transpose_b, dtype, num_iters)
