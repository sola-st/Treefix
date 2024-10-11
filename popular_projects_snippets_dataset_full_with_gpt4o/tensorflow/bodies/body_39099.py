# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
labels = [[3, 2], [0, 3]]
logits = [[[1., 1., 1., 1.], [2., 2., 2., 2.]],
          [[1., 2., 3., 4.], [5., 6., 7., 8.]]]
self._testHighDim(labels, logits)
