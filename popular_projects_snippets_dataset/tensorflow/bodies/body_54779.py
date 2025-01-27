# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
tf_val = math_ops.cast(constant_op.constant([-1, 1, -1]), dtypes.int64)
c_val = tensor_util.constant_value_as_shape(tf_val)
self.assertEqual([None, 1, None], c_val.as_list())
