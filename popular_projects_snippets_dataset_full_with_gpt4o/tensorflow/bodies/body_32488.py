# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
placeholder = array_ops.placeholder(dtypes.int32, shape=(None, None, 3))
with self.assertRaises(ValueError):
    check_ops.ensure_shape(placeholder, (2, 3))
