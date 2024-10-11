# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
with ops.Graph().as_default():
    tf_val = gen_state_ops.variable(
        shape=[3, 4, 7],
        dtype=dtypes.float32,
        name="tf_val",
        container="",
        shared_name="")
    self.assertIs(None, tensor_util.constant_value(tf_val))
