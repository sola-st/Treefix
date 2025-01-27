# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
input_ = np.random.rand(4, 7)
# This test needs a placeholder which means we need to construct a graph.
with ops.Graph().as_default():
    placeholder = array_ops.placeholder(dtypes.float32, shape=(4, 7))
    # it'd be better to use concat here, but concat doesn't support partial
    packed = array_ops.stack([input_, placeholder])
    tf_vals = array_ops.split(packed, 2)
    c_vals = [tensor_util.constant_value(x, partial=True) for x in tf_vals]
    self.assertAllClose(input_, c_vals[0][0])
    self.assertIsNone(c_vals[1][0])
