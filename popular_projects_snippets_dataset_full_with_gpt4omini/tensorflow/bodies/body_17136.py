# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# In this test inputs get converted to EagerTensors before calling the
# tf.function. The error message here is raised in python
# since the python function has direct access to the tensor's values.
with context.eager_mode():
    x_shape = [3, 3, 1]
    x = np.zeros(x_shape)

    # Each line is a test configuration:
    #   offset_height, offset_width, target_height, target_width, err_msg
    test_config = (
        (-1, 0, 4, 4,
         "offset_height must be >= 0"),
        (0, -1, 4, 4,
         "offset_width must be >= 0"),
        (2, 0, 4, 4,
         "height must be <= target - offset"),
        (0, 2, 4, 4,
         "width must be <= target - offset"))
    for config_item in test_config:
        self._assertRaises(
            x, x_shape, *config_item, use_tensor_inputs_options=[True])
