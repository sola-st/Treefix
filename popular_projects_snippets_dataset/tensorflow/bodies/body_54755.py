# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
np_val = np.array([-1, -1, -1], dtype=np.float32)
tf_val = array_ops.fill([3], constant_op.constant(-1.0))
c_val = tensor_util.constant_value(tf_val)
self.assertAllEqual(np_val, c_val)
self.assertEqual(np.float32, c_val.dtype)
