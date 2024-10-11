# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
tf_val = array_ops.size(constant_op.constant(0.0, shape=[1, 2, 3]))
c_val = tensor_util.constant_value(tf_val)
self.assertEqual(6, c_val)
