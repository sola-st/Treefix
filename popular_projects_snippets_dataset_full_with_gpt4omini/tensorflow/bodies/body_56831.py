# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/transpose_conv.py
"""Build a transpose_conv graph given `parameters`."""
input_shape, filter_shape = get_tensor_shapes(parameters)
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=input_shape)

filter_input = tf.compat.v1.placeholder(
    dtype=tf.float32, name="filter", shape=filter_shape)

if not parameters["const_weight_bias"]:
    input_tensors = [input_tensor, filter_input]
    conv_outputs = tf.nn.conv2d(
        input=input_tensor,
        filters=filter_input,
        strides=parameters["strides"],
        padding=parameters["padding"],
        data_format=parameters["data_format"])
    out = tf.compat.v1.nn.conv2d_backprop_input(
        input_shape,
        filter_input,
        conv_outputs,
        strides=parameters["strides"],
        padding=parameters["padding"],
        data_format=parameters["data_format"])
else:
    input_tensors = [input_tensor]
    if parameters["fully_quantize"]:
        filter_input = create_tensor_data(
            np.float32, filter_shape, min_value=-1, max_value=1)
    else:
        filter_input = create_tensor_data(np.float32, filter_shape)
    out = tf.nn.conv2d_transpose(
        input_tensor,
        filter_input,
        parameters["output_shape"],
        strides=parameters["strides"],
        padding=parameters["padding"],
        data_format=parameters["data_format"])
    if parameters["has_bias"]:
        if parameters["fully_quantize"]:
            bias_input = create_tensor_data(
                np.float32, (parameters["output_shape"][-1],),
                min_value=-1,
                max_value=1)
        else:
            bias_input = create_tensor_data(np.float32,
                                            (parameters["output_shape"][-1],))
        out = tf.nn.bias_add(
            out, bias_input, data_format=parameters["data_format"])

        mul_data = create_tensor_data(np.float32,
                                      (parameters["output_shape"][-1],))
        out = tf.math.multiply(out, mul_data)

exit((input_tensors, [out]))
