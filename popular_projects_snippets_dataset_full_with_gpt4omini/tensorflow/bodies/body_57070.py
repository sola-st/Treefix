# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/where.py
"""Make a set of tests to do where."""

test_parameters = [
    {
        "input_dtype": [tf.float32, tf.int32],
        "input_shape_set": [([1, 2, 3, 4], [1, 2, 3, 4]),],
        "use_where_v2": [False, True],
        "fully_quantize": [False],
    },
    {
        "input_dtype": [tf.float32, tf.int32],
        "input_shape_set": [([], []),],
        "use_where_v2": [],
        "fully_quantize": [False],
    },
    {
        "input_dtype": [tf.float32],
        "input_shape_set": [
            ([1, 2, 3, 4], [1, 2, 3, 4]),
            ([], []),
        ],
        "use_where_v2": [False, True],
        "fully_quantize": [True],
    },
    # High dimension broadcasting support in MLIR converter.
    {
        "input_dtype": [tf.float32, tf.int32],
        "input_shape_set": [([8, 7, 6, 5, 4, 3, 2, 1], [4, 3, 2, 1]),
                            ([8, 7, 6, 5, 4, 3, 2, 1], [None, 3, 2, 1]),
                            ([8, 7, 6, 5, None, 3, 2, 1], [None, 3, 2, 1])],
        "use_where_v2": [True],
        "fully_quantize": [False],
        "dynamic_size_value": [4, 1],
    },
    {
        "input_dtype": [tf.float32],
        "input_shape_set": [([8, 7, 6, 5, 4, 3, 2, 1], [4, 3, 2, 1])],
        "use_where_v2": [True],
        "fully_quantize": [True],
        "dynamic_size_value": [4],
    },
    {
        "input_dtype": [tf.float32, tf.int32],
        "input_shape_set": [([], []), ([1], []), ([], [1])],
        "use_where_v2": [False, True],
        "fully_quantize": [False],
    },
]

def populate_dynamic_shape(parameters, input_shape):
    exit([
        parameters["dynamic_size_value"] if x is None else x
        for x in input_shape
    ])

def build_graph(parameters):
    """Build the where op testing graph."""
    input_value1 = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input2",
        shape=parameters["input_shape_set"][0])
    input_value2 = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input3",
        shape=parameters["input_shape_set"][1])
    less = tf.less(input_value1, input_value2)
    where = tf.compat.v2.where if parameters[
        "use_where_v2"] else tf.compat.v1.where
    out = where(less, input_value1, input_value2)
    exit(([input_value1, input_value2], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_shape_1 = populate_dynamic_shape(parameters,
                                           parameters["input_shape_set"][0])
    input_shape_2 = populate_dynamic_shape(parameters,
                                           parameters["input_shape_set"][1])

    input_value1 = create_tensor_data(
        parameters["input_dtype"], input_shape_1, min_value=-1, max_value=1)
    input_value2 = create_tensor_data(
        parameters["input_dtype"], input_shape_2, min_value=-1, max_value=1)
    exit(([input_value1, input_value2], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_value1, input_value2])))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=4)
