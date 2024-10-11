# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/transpose_conv.py
input_shape, filter_shape = get_tensor_shapes(parameters)
if not parameters["const_weight_bias"]:
    values = [
        create_tensor_data(np.float32, input_shape),
        create_tensor_data(np.float32, filter_shape)
    ]
else:
    if parameters["fully_quantize"]:
        values = [
            create_tensor_data(
                np.float32, input_shape, min_value=-1, max_value=1),
        ]
    else:
        values = [create_tensor_data(np.float32, input_shape),]

exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
