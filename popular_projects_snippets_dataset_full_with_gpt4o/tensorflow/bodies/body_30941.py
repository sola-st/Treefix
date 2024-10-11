# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
labels = [
    [3, 4, 4, 3],
    [1, 1, 1, 0],
]
unique, idx = ctc_ops.ctc_unique_labels(labels)
self.assertAllEqual([
    [3, 4, 0, 0],
    [1, 0, 0, 0],
], unique)
self.assertAllEqual([
    [0, 1, 1, 0],
    [0, 0, 0, 1],
], idx)
