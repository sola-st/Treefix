# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/sign.py
"""Make a set of tests to do sign."""

test_parameters = [{
    "input_dtype": [tf.float32, tf.float64],
    "input_shape": [[], [1], [1, 2], [5, 6, 7, 8], [3, 4, 5, 6]],
}]

def build_graph(parameters):
    """Build the sign op testing graph."""
    input_value = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input1",
        shape=parameters["input_shape"])
    out = tf.math.sign(input_value)
    exit(([input_value], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_value = create_tensor_data(parameters["input_dtype"],
                                     parameters["input_shape"])
    exit(([input_value], sess.run(outputs, dict(zip(inputs, [input_value])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
