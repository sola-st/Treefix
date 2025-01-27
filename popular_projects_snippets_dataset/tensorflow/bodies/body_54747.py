# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
np_val = np.random.rand(3).astype(np.int32)
tf_val = constant_op.constant(np_val)
self.assertFalse(tensor_util.is_tf_type(np_val))
self.assertTrue(tensor_util.is_tf_type(tf_val))
