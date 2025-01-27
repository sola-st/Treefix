# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/equal.py
"""Make a set of tests to do equal."""

test_parameters = [{
    "input_dtype": [tf.float32, tf.int32, tf.int64, tf.string],
    "input_shape_pair": [([], []), ([1, 1, 1, 3], [1, 1, 1, 3]),
                         ([2, 3, 4, 5], [2, 3, 4, 5]), ([2, 3, 3], [2, 3]),
                         ([5, 5], [1]), ([10], [2, 4, 10])],
    "fully_quantize": [False],
}, {
    "input_dtype": [tf.float32],
    "input_shape_pair": [([1, 1, 1, 3], [1, 1, 1, 3]), ([2, 3, 3], [2, 3])],
    "fully_quantize": [True],
}]

def build_graph(parameters):
    """Build the equal op testing graph."""
    input_value1 = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input1",
        shape=parameters["input_shape_pair"][0])
    input_value2 = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input2",
        shape=parameters["input_shape_pair"][1])
    out = tf.equal(input_value1, input_value2)
    exit(([input_value1, input_value2], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_value1 = create_tensor_data(parameters["input_dtype"],
                                      parameters["input_shape_pair"][0])
    input_value2 = create_tensor_data(parameters["input_dtype"],
                                      parameters["input_shape_pair"][1])
    exit(([input_value1, input_value2], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value1, input_value2])))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=5)
