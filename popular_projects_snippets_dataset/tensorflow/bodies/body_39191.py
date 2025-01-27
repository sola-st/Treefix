# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
self.assertAllEqual(
    self._MakeAndReshapeTensor(tensor_class, [2, 4, 0, 6], [-1, 4, 6, 2]),
    [0, 4, 6, 2])
