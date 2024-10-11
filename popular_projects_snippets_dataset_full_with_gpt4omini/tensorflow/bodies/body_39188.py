# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
self.assertAllEqual(
    self._MakeAndReshapeTensor(tensor_class, [0], [-1, 1]), [0, 1])
self.assertAllEqual(
    self._MakeAndReshapeTensor(tensor_class, [0], [-1, 1, 2]), [0, 1, 2])
