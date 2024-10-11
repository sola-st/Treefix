# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/random_standard_normal.py
"""Make a set of tests to do random_standard_normal."""

test_parameters = [{
    "input_shape": [[1]],
    "input_dtype": [tf.int32],
    "shape": [[10]],
    "seed": [None, 0, 1234],
    "seed2": [0, 5678],
    "dtype": [tf.float32],
}, {
    "input_shape": [[3]],
    "input_dtype": [tf.int32],
    "shape": [[2, 3, 4]],
    "seed": [0, 1234],
    "seed2": [None, 0, 5678],
    "dtype": [tf.float32],
}]

def build_graph(parameters):
    """Build the op testing graph."""
    tf.compat.v1.set_random_seed(seed=parameters["seed"])
    input_value = tf.compat.v1.placeholder(
        name="shape",
        shape=parameters["input_shape"],
        dtype=parameters["input_dtype"])
    out = tf.random.normal(
        shape=input_value, dtype=parameters["dtype"], seed=parameters["seed2"])
    exit(([input_value], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_value = create_tensor_data(
        parameters["input_dtype"],
        parameters["input_shape"],
        min_value=1,
        max_value=10)
    exit(([input_value], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
