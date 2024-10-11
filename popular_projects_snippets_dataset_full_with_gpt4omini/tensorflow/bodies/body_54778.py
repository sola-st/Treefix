# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
tf_val = math_ops.cast(
    array_ops.shape(constant_op.constant(0.0, shape=[1, 2, 3])),
    dtypes.int64)
c_val = tensor_util.constant_value_as_shape(tf_val)
self.assertEqual(tensor_shape.TensorShape([1, 2, 3]), c_val)
