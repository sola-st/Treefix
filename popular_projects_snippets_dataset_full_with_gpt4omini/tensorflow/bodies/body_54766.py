# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
input_ = np.random.rand(4, 7)
# This test needs a placeholder which means we need to construct a graph.
with ops.Graph().as_default():
    packed = array_ops.stack([input_, array_ops.placeholder(dtypes.float32)])
    tf_vals = array_ops.unstack(packed)
    c_vals = [tensor_util.constant_value(x, partial=True) for x in tf_vals]
    self.assertAllClose(input_, c_vals[0])
    self.assertIsNone(c_vals[1])
