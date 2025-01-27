# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_arrays_test.py
a = ops.convert_to_tensor(value=[1.0, 2.0])
self.assertAllEqual([-1.0, -2.0], -a)  # pylint: disable=invalid-unary-operand-type
