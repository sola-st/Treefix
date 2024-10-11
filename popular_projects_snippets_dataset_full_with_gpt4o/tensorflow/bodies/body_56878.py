# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/tile.py
"""Make a set of tests to do tile."""
test_parameters = [
    {
        "input_dtype": [tf.float32, tf.int32, tf.bool, tf.string],
        "input_shape": [[3, 2, 1], [2, 2, 2]],
        "multiplier_dtype": [tf.int32, tf.int64],
        "multiplier_shape": [[3]]
    },
    {
        "input_dtype": [tf.float32, tf.int32],
        "input_shape": [[]],
        "multiplier_dtype": [tf.int32, tf.int64],
        "multiplier_shape": [[0]]
    },
    {
        "input_dtype": [tf.float32],
        "input_shape": [[3, 2, 1]],
        "multiplier_dtype": [tf.int32, tf.int64],
        "multiplier_shape": [[3]],
        "fully_quantize": [True],
        # The input range is used to create representative dataset for both
        # input and multiplier so it needs to be positive.
        "input_range": [(1, 10)],
    }
]

def build_graph(parameters):
    """Build the tile op testing graph."""
    input_value = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        shape=parameters["input_shape"],
        name="input")
    multiplier_value = tf.compat.v1.placeholder(
        dtype=parameters["multiplier_dtype"],
        shape=parameters["multiplier_shape"],
        name="multiplier")
    out = tf.tile(input_value, multiplier_value)
    exit(([input_value, multiplier_value], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    min_value, max_value = parameters.get("input_range", (-10, 10))
    input_value = create_tensor_data(
        parameters["input_dtype"],
        parameters["input_shape"],
        min_value=min_value,
        max_value=max_value)
    multipliers_value = create_tensor_data(
        parameters["multiplier_dtype"],
        parameters["multiplier_shape"],
        min_value=0)
    exit(([input_value, multipliers_value], sess.run(
        outputs,
        feed_dict={
            inputs[0]: input_value,
            inputs[1]: multipliers_value
        })))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
