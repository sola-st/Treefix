# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
input_ = np.random.rand(4, 7)
# This test needs a placeholder which means we need to construct a graph.
with ops.Graph().as_default():
    tf_val = array_ops.stack([input_, array_ops.placeholder(dtypes.float32)])
    c_val = tensor_util.constant_value(tf_val, partial=True)
    self.assertAllClose(input_, c_val[0])
    self.assertIsNone(c_val[1])
