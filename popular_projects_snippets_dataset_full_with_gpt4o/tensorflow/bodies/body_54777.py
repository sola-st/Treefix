# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
np_val = np.random.rand(3).astype(np.int32)
tf_val = constant_op.constant(np_val)
self.assertEqual(
    tensor_shape.TensorShape(np_val),
    tensor_util.constant_value_as_shape(tf_val))

tf_val = constant_op.constant([], dtype=dtypes.int32)
self.assertEqual(
    tensor_shape.TensorShape([]),
    tensor_util.constant_value_as_shape(tf_val))
