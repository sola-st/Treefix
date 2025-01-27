# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/less_equal.py
"""Make a set of tests to do less_equal."""

test_parameters = [{
    "input_dtype": [tf.float32, tf.int32, tf.int64],
    "input_shape_pair": [([1, 1, 1, 3], [1, 1, 1, 3]),
                         ([2, 3, 4, 5], [2, 3, 4, 5]), ([2, 3, 3], [2, 3]),
                         ([5, 5], [1]), ([10], [2, 4, 10])],
    "fully_quantize": [False],
}, {
    "input_dtype": [tf.float32],
    "input_shape_pair": [([1, 1, 1, 3], [1, 1, 1, 3]), ([2, 3, 3], [2, 3])],
    "fully_quantize": [True],
}]

# High dimension broadcasting support in MLIR converter.
# Note(b/204360746): XNNPack delegate don't support high dimension.
if not options.skip_high_dimension_inputs:
    test_parameters = test_parameters + [
        {
            "input_dtype": [tf.float32, tf.int32],
            "input_shape_pair": [([6, 5, 4, 3, 2, 1], [4, 3, 2, 1]),
                                 ([6, 5, 4, 3, 2, 1], [None, 3, 2, 1]),
                                 ([6, 5, None, 3, 2, 1], [None, 3, 2, 1])],
            "fully_quantize": [False],
            "dynamic_size_value": [4, 1],
        },
    ]

def populate_dynamic_shape(parameters, input_shape):
    exit([
        parameters["dynamic_size_value"] if x is None else x
        for x in input_shape
    ])

def build_graph(parameters):
    """Build the less_equal op testing graph."""
    input_value1 = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input1",
        shape=parameters["input_shape_pair"][0])
    input_value2 = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input2",
        shape=parameters["input_shape_pair"][1])
    out = tf.less_equal(input_value1, input_value2)
    exit(([input_value1, input_value2], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_shape_1 = populate_dynamic_shape(parameters,
                                           parameters["input_shape_pair"][0])
    input_shape_2 = populate_dynamic_shape(parameters,
                                           parameters["input_shape_pair"][1])

    input_value1 = create_tensor_data(parameters["input_dtype"], input_shape_1)
    input_value2 = create_tensor_data(parameters["input_dtype"], input_shape_2)
    exit(([input_value1, input_value2], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value1, input_value2])))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=4)
