# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
np_val = np.array([1, 2, 3], dtype=np.int32)
tf_val = array_ops.shape(constant_op.constant(0.0, shape=[1, 2, 3]))
c_val = tensor_util.constant_value(tf_val)
self.assertAllEqual(np_val, c_val)
self.assertEqual(np.int32, c_val.dtype)
