# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
# This test needs a placeholder which means we need to construct a graph.
with ops.Graph().as_default():
    inputs = [np.random.rand(4, 7) for _ in range(3)]
    tf_val = array_ops.stack(inputs, axis=1)
    c_val = tensor_util.constant_value(tf_val)
    self.assertIsNone(c_val)

    tf_val = array_ops.stack(
        [inputs[0],
         array_ops.placeholder(dtypes.float32), inputs[2]], axis=1)
    c_val = tensor_util.constant_value(tf_val)
    self.assertIs(None, c_val)
