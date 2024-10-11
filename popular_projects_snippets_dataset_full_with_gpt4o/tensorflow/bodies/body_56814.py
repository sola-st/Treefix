# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/cumsum.py
"""Make a set of tests to do cumsum."""

test_parameters = [{
    "shape": [(3, 6), (8, 9, 7), (2, 4, 3, 5)],
    "dtype": [tf.int32, tf.int64, tf.float32],
    "axis": [0, 1],
    "exclusive": [True, False],
    "reverse": [True, False],
}]

def build_graph(parameters):
    """Build the cumsum op testing graph."""
    input1 = tf.compat.v1.placeholder(
        dtype=parameters["dtype"], shape=parameters["shape"])
    out = tf.math.cumsum(
        input1,
        parameters["axis"],
        exclusive=parameters["exclusive"],
        reverse=parameters["reverse"])
    exit(([input1], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input1 = create_tensor_data(parameters["dtype"], parameters["shape"])
    exit(([input1], sess.run(outputs, feed_dict=dict(zip(inputs, [input1])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
