# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# In this test inputs get converted to tensors before calling the
# tf.function. The error message here is raised during shape inference.
with context.graph_mode():
    x_shape = [3, 3, 1]
    x = np.zeros(x_shape)
    self._assertRaises(
        x,
        x_shape,
        *config,
        "Paddings must be non-negative",
        use_tensor_inputs_options=[True])
