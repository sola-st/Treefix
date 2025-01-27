# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
self.assertAllEqual(output.indices,
                    [[0, 0], [1, 13], [1, 10], [2, 33], [2, 32], [1, 14]])
self.assertAllEqual(output.values, [-3, 4, 1, 9, 5, 1])
self.assertAllEqual(output.dense_shape, [3, vocab_size])
