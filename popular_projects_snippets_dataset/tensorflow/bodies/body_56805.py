# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv_bias_activation.py
"""Build inputs for conv with activation."""

input_shape, _ = get_tensor_shapes(parameters)
values = [
    create_tensor_data(
        np.float32, input_shape, min_value=-1, max_value=1)
]
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
