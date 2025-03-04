# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/expand_dims.py
"""Make a set of tests to do expand_dims."""

test_parameters = [{
    "input_type": [tf.float32, tf.int32],
    "input_shape": [[5, 4], [1, 5, 4]],
    "axis_value": [0, 1, 2, -1, -2, -3],
    "constant_axis": [True, False],
    "fully_quantize": [False],
}, {
    "input_type": [tf.float32],
    "input_shape": [[5, 4], [1, 5, 4]],
    "axis_value": [0, 1, 2, -1, -2, -3],
    "constant_axis": [True],
    "fully_quantize": [True],
}]

def build_graph(parameters):
    """Build the where op testing graph."""
    inputs = []
    input_value = tf.compat.v1.placeholder(
        dtype=parameters["input_type"],
        name="input",
        shape=parameters["input_shape"])
    inputs.append(input_value)

    if parameters["constant_axis"]:
        axis_value = tf.constant(
            parameters["axis_value"], dtype=tf.int32, shape=[1])
    else:
        axis_value = tf.compat.v1.placeholder(
            dtype=tf.int32, name="axis", shape=[1])
        inputs.append(axis_value)

    out = tf.expand_dims(input_value, axis=axis_value)
    exit((inputs, [out]))

def build_inputs(parameters, sess, inputs, outputs):
    """Builds the inputs for expand_dims."""
    input_values = []
    input_values.append(
        create_tensor_data(
            parameters["input_type"],
            parameters["input_shape"],
            min_value=-1,
            max_value=1))
    if not parameters["constant_axis"]:
        input_values.append(np.array([parameters["axis_value"]], dtype=np.int32))
    exit((input_values, sess.run(
        outputs, feed_dict=dict(zip(inputs, input_values)))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
