# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
super(AbsoluteDifferenceLossTest, self).setUp()
self._predictions = constant_op.constant([4, 8, 12, 8, 1, 3], shape=(2, 3))
self._labels = constant_op.constant([1, 9, 2, -5, -2, 6], shape=(2, 3))
