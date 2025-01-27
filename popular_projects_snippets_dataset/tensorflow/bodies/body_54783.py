# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
# This test needs a placeholder which means we need to construct a graph.
with ops.Graph().as_default():
    tf_val = array_ops.concat(
        [[16, 37], array_ops.placeholder(dtypes.int32, shape=(2,))], 0)
    c_val = tensor_util.constant_value_as_shape(tf_val)
    self.assertEqual([16, 37, None, None], c_val.as_list())

    tf_val = array_ops.concat(
        [[16, 37],
         array_ops.placeholder(dtypes.int32, shape=(1,)), [48]], 0)
    c_val = tensor_util.constant_value_as_shape(tf_val)
    self.assertEqual([16, 37, None, 48], c_val.as_list())
