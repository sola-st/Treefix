# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/maximum.py
"""Make a set of tests to do maximum."""

test_parameters = [{
    "input_dtype": [tf.float32],
    "input_shape_1": [[], [3], [1, 100], [4, 2, 3], [5, 224, 224, 3],
                      [5, 32, 32, 3, 1], [5, 32, 32, 3, 1]],
    "input_shape_2": [[], [3], [1, 100], [4, 2, 3], [5, 224, 224, 3],
                      [5, 32, 32, 3, 3], [5, 32, 32, 3, 1]],
    "fully_quantize": [False, True],
}]

def build_graph(parameters):
    """Build the maximum op testing graph."""
    input_tensor_1 = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input_1",
        shape=parameters["input_shape_1"])
    input_tensor_2 = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input_2",
        shape=parameters["input_shape_2"])

    out = tf.maximum(input_tensor_1, input_tensor_2)
    exit(([input_tensor_1, input_tensor_2], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    """Builds the inputs for the model above."""
    values = [
        create_tensor_data(
            parameters["input_dtype"],
            parameters["input_shape_1"],
            min_value=-1,
            max_value=1),
        create_tensor_data(
            parameters["input_dtype"],
            parameters["input_shape_2"],
            min_value=-1,
            max_value=1)
    ]
    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=44)
