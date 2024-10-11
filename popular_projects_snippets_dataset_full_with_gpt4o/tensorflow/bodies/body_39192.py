# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
# NOTE: When implied dimensions and zero dimensions coexist in the target
# shape, the behavior currently differs between sparse and regular tensors.
with self.assertRaises(errors.InvalidArgumentError):
    self._MakeAndReshapeTensor("sparse", [0], [-1, 0])
with self.assertRaises(errors.InvalidArgumentError):
    self._MakeAndReshapeTensor("sparse", [1, 0], [-1, 0])
with self.assertRaises(errors.InvalidArgumentError):
    self._MakeAndReshapeTensor("sparse", [1, 2, 0], [2, -1, 0])
with self.assertRaises(errors.InvalidArgumentError):
    self._MakeAndReshapeTensor("sparse", [1, 2, 3, 0], [2, 0, -1, 3])
