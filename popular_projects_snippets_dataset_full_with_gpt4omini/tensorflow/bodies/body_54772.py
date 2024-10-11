# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
input_ = np.random.rand(4, 7)
tf_val = array_ops.identity(input_)
c_val = tensor_util.constant_value(tf_val)
self.assertAllEqual(input_, c_val)
