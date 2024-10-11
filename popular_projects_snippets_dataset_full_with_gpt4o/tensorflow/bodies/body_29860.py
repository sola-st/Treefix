# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
d = array_ops.placeholder(dtypes_lib.float32, shape=[None, 4, None])
z = array_ops.zeros_like(d)
self.assertEqual(d.get_shape().as_list(), z.get_shape().as_list())
