# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
tf_val = constant_op.constant([-1, 1, -1], shape=[3])
c_val = tensor_util.constant_value_as_shape(tf_val)
self.assertEqual([None, 1, None], c_val.as_list())
