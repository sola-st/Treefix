# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/rank.py
"""Make a set of tests to do rank."""

test_parameters = [{
    "input_dtype": [tf.float32, tf.int32],
    "input_shape": [[], [0], [1, 1, 1, 3], [2, 3, 4, 5], [5, 5], [10]],
}]

def build_graph(parameters):
    """Build the rank op testing graph."""
    input_value = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"], name="input")
    out = tf.rank(input_value)
    exit(([input_value], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_value = create_tensor_data(parameters["input_dtype"],
                                     parameters["input_shape"])
    exit(([input_value], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
