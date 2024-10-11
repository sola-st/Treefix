# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
inputs = np.random.rand(3, 4, 7)
tf_vals = array_ops.unstack(inputs)
c_vals = [tensor_util.constant_value(x) for x in tf_vals]
self.assertAllClose(inputs, c_vals)
