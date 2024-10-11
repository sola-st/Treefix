# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/hardswish.py
"""Make a set of tests to do hardswish."""

# Chose a set of parameters
if options.run_with_flex:
    # Only Flex is able to execute on the data bigger than four dimension.
    test_parameters = [{
        "input_shape": [[], [1], [2, 3], [1, 1, 1, 1], [1, 3, 4, 3],
                        [3, 15, 14, 3], [3, 1, 2, 4, 6], [2, 2, 3, 4, 5, 6]],
    }]
else:
    test_parameters = [{
        "input_shape": [[], [1], [2, 3], [1, 1, 1, 1], [1, 3, 4, 3],
                        [3, 15, 14, 3]],
    }]

def build_graph(parameters):
    inp = tf.compat.v1.placeholder(
        dtype=tf.float32, name="input", shape=parameters["input_shape"])
    out = inp * tf.nn.relu6(inp + np.float32(3)) * np.float32(1. / 6.)

    exit(([inp], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_values = create_tensor_data(
        np.float32, parameters["input_shape"], min_value=-10, max_value=10)
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

# Add additional validation if we are using converter.
# Flex doesn't yet support this.
if not options.run_with_flex:
    options.tflite_convert_function = functools.partial(
        _tflite_convert_verify_num_ops,
        options.tflite_convert_function,
        num_ops=2)
make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
