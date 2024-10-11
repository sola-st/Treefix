# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
self.assertAllEqual(output.indices,
                    [[0, 0], [1, 10], [1, 13], [1, 14], [2, 32], [2, 33]])
self.assertAllEqual(output.values, [-3, 1, 4, 1, 5, 9])
self.assertAllEqual(output.dense_shape, [3, vocab_size])
