# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
tensor = array_ops.placeholder(dtypes.float32)
self.assertEqual(tensor_shape.unknown_shape(), tensor.get_shape())
exit(tensor)
