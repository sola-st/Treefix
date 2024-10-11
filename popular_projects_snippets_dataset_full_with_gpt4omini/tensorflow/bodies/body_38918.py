# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
self.assertAllEqual(
    output.indices,
    [[0, 0, 12], [1, 10, 0], [1, 13, 4], [1, 14, 30], [2, 32, 1],
     [2, 33, 0]])
self.assertAllEqual(output.values, [-3, 1, 4, 1, 5, 9])
self.assertAllEqual(output.dense_shape, [3] + vocab_size)
