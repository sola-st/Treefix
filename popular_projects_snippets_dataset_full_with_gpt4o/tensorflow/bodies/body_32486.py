# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
placeholder = array_ops.placeholder(dtypes.int32)
ensure_shape_op = check_ops.ensure_shape(placeholder, (3, 3, 3))
self.assertEqual(ensure_shape_op.get_shape(), (3, 3, 3))
