# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
tf_val = array_ops.rank(constant_op.constant(0.0, shape=[1, 2, 3]))
c_val = tensor_util.constant_value(tf_val)

self.assertIn(type(c_val), [np.ndarray, np.int32])
self.assertEqual((), c_val.shape)
self.assertEqual(3, c_val)

# Repeat test using array_ops.rank_internal to avoid the optimization that
# happens in the rank function.
tf_val = array_ops.rank_internal(
    constant_op.constant(
        0.0, shape=[1, 2, 3]), optimize=False)
c_val = tensor_util.constant_value(tf_val)

self.assertIn(type(c_val), [np.ndarray, np.int32])
self.assertEqual((), c_val.shape)
self.assertEqual(3, c_val)
self.assertEqual([3], c_val)
