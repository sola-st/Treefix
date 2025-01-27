# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
placeholder = array_ops.placeholder(dtypes.int32, shape=(None, None, 3))
ensure_shape_op = check_ops.ensure_shape(placeholder, (5, 4, None))
self.assertEqual(ensure_shape_op.get_shape(), (5, 4, 3))
