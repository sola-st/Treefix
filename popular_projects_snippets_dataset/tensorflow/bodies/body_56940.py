# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/one_hot.py
"""Make a set of tests to do one_hot."""

test_parameters = [{
    "indices_type": [tf.int32, tf.int64],
    "indices_shape": [[3], [4, 4], [1, 5], [5, 1]],
    "axis": [0, 1],
    "dtype": [tf.int32, tf.int64, tf.float32],
    "provide_optional_inputs": [True, False],
}]

def build_graph(parameters):
    """Build the one_hot op testing graph."""
    indices = tf.compat.v1.placeholder(
        dtype=parameters["indices_type"],
        name="indices",
        shape=parameters["indices_shape"])
    depth = tf.compat.v1.placeholder(dtype=tf.int32, name="depth", shape=())

    if not parameters["provide_optional_inputs"]:
        out = tf.one_hot(indices=indices, depth=depth)
        exit(([indices, depth], [out]))

    on_value = tf.compat.v1.placeholder(
        dtype=parameters["dtype"], name="on_value", shape=())
    off_value = tf.compat.v1.placeholder(
        dtype=parameters["dtype"], name="off_value", shape=())
    out = tf.one_hot(
        indices=indices,
        depth=depth,
        on_value=on_value,
        off_value=off_value,
        axis=parameters["axis"],
        dtype=parameters["dtype"])
    exit(([indices, depth, on_value, off_value], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    """Build the input for one_hot op."""
    input_values = [
        create_tensor_data(
            parameters["indices_type"],
            shape=parameters["indices_shape"],
            min_value=-1,
            max_value=10),
        create_tensor_data(tf.int32, shape=None, min_value=1, max_value=10),
    ]

    if parameters["provide_optional_inputs"]:
        input_values.append(
            create_tensor_data(
                parameters["dtype"], shape=None, min_value=1, max_value=10))
        input_values.append(
            create_tensor_data(
                parameters["dtype"], shape=None, min_value=-1, max_value=0))

    exit((input_values, sess.run(
        outputs, feed_dict=dict(zip(inputs, input_values)))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
