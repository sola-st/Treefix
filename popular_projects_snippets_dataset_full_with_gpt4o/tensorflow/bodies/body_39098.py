# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
labels = [[3], [0]]
logits = [[[1., 1., 1., 1.]], [[1., 2., 3., 4.]]]
self._testHighDim(labels, logits)
