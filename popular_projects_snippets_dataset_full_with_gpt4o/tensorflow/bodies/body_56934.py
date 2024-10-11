# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/gelu.py
"""Makes a set of tests for gelu."""

test_parameters = [{
    "input_dtype": [tf.float32],
    "input_shape": [[], [1], [2, 3], [1, 1, 1, 1], [1, 3, 4, 3],
                    [3, 15, 14, 3], [3, 1, 2, 4, 6], [2, 2, 3, 4, 5, 6]],
    "fully_quantize": [False, True],
    "input_range": [(-10, 10)],
    "approximate": [True, False],
}]

def build_graph(parameters):
    """Builds the gelu op testing graph."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])

    out = tf.nn.gelu(input_tensor, approximate=parameters["approximate"])
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    values = [
        create_tensor_data(
            parameters["input_dtype"],
            parameters["input_shape"],
            min_value=-8,
            max_value=8)
    ]
    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

if not options.run_with_flex:
    options.tflite_convert_function = functools.partial(
        _tflite_convert_verify_op,
        options.tflite_convert_function)
make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
