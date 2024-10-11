# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
np_val = np.random.rand(3, 4, 7).astype(np.float32)
tf_val = math_ops.cast(constant_op.constant(np_val), dtypes.float64)
c_val = tensor_util.constant_value(tf_val)
self.assertAllClose(np_val.astype(np.float64), c_val)

np_val = np.random.rand(3, 0, 7).astype(np.float32)
tf_val = math_ops.cast(constant_op.constant(np_val), dtypes.float64)
c_val = tensor_util.constant_value(tf_val)
self.assertAllClose(np_val.astype(np.float64), c_val)
