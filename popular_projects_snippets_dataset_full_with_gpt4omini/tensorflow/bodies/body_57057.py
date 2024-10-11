# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/fill.py
"""Make a set of tests to do fill."""

test_parameters = [{
    "dims_dtype": [tf.int32, tf.int64],
    "dims_shape": [[], [1], [3], [3, 3]],
    "value_dtype": [tf.int32, tf.int64, tf.float32, tf.bool, tf.string],
}]

def build_graph(parameters):
    """Build the fill op testing graph."""
    input1 = tf.compat.v1.placeholder(
        dtype=parameters["dims_dtype"],
        name="dims",
        shape=parameters["dims_shape"])
    input2 = tf.compat.v1.placeholder(
        dtype=parameters["value_dtype"], name="value", shape=[])
    out = tf.fill(input1, input2)
    exit(([input1, input2], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input1 = create_tensor_data(parameters["dims_dtype"],
                                parameters["dims_shape"], 1)
    input2 = create_scalar_data(parameters["value_dtype"])
    exit(([input1, input2], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input1, input2])))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=20)
