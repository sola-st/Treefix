# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
x = ops.convert_to_tensor(10.0)
self.assertTrue(isinstance(x, ops.EagerTensor))
