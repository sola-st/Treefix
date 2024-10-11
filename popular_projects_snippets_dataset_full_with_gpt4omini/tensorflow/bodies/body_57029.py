# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/constant.py
"""Make a set of tests to do constant ops."""

test_parameters = [{
    "dtype": [tf.float32, tf.int32],
    "input_shape": [[], [1], [2], [1, 1, 1, 1], [2, 2, 2, 2]],
    "constant_is_also_output": [True, False],
    # Models should not be rejected regardless whether it has unread inputs.
    "has_unread_input": [True, False],
}]

def build_graph(parameters):
    """Build a constant graph given `parameters`."""
    dummy_input = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input1",
        shape=parameters["input_shape"])
    constant = tf.constant(
        create_tensor_data(parameters["dtype"], parameters["input_shape"]))
    outputs = [tf.maximum(dummy_input, constant)]
    if parameters["constant_is_also_output"]:
        outputs.append(constant)
    inputs = [dummy_input]
    if parameters["has_unread_input"]:
        unread_input = tf.compat.v1.placeholder(
            dtype=parameters["dtype"],
            name="unread_input",
            shape=parameters["input_shape"])
        inputs.append(unread_input)

    exit((inputs, outputs))

def build_inputs(parameters, sess, inputs, outputs):
    dummy_input = np.zeros(
        parameters["input_shape"],
        dtype=MAP_TF_TO_NUMPY_TYPE[parameters["dtype"]])
    exit(([dummy_input], sess.run(outputs, feed_dict={inputs[0]: dummy_input})))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
