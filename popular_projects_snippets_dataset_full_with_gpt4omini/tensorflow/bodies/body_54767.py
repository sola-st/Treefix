# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
inputs = np.random.rand(6, 5, 7)
tf_vals = array_ops.split(inputs, 3)
c_vals = [tensor_util.constant_value(x) for x in tf_vals]
self.assertAllClose(np.split(inputs, 3), c_vals)
