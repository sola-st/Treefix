# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv_with_shared_weights.py
# Build list of input values either containing 1 tensor (input) or 2 tensors
# (input, filter) based on whether filter is constant or variable input.
input_shape, unused_filter_shape = get_tensor_shapes(parameters)
values = [create_tensor_data(np.float32, input_shape)]
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
