# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
np_val = np.random.rand(3, 4, 7).astype(np.float32)
tf_val = array_ops.concat(
    [np_val[0:1, :, :], np_val[1:2, :, :], np_val[2:3, :, :]], 0)
c_val = tensor_util.constant_value(tf_val)
self.assertAllClose(np_val, c_val)

# This test needs a placeholder which means we need to construct a graph.
with ops.Graph().as_default():
    tf_val = array_ops.concat(
        [np_val[0, :, :], np_val[1, :, :], np_val[2, :, :]],
        array_ops.placeholder(dtypes.int32))
    c_val = tensor_util.constant_value(tf_val)
    self.assertIs(None, c_val)

    tf_val = array_ops.concat([
        np_val[0, :, :],
        array_ops.placeholder(dtypes.float32), np_val[2, :, :]
    ], 1)
    c_val = tensor_util.constant_value(tf_val)
    self.assertIs(None, c_val)
