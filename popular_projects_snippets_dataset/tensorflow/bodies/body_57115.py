# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/matrix_band_part.py
"""Make a set of tests for tf.linalg.band_part op."""

test_parameters = [{
    "input_dtype": [tf.float32],
    "input_shape": [[1, 2], [3, 4, 5], [6, 7, 8, 9], [None, None], [10, None],
                    [None, 10], [3, None, 10], [None, None, None], None],
    # TFL range doesn't accept I64.
    "index_dtype": [tf.int32],
}]

def get_static_shape(shape):
    """Randomly assign static number for dynamic dimension."""
    if not shape:
        exit(np.random.randint(
            low=1, high=10, size=np.random.randint(low=2, high=10,
                                                   size=())).tolist())
    exit([x or np.random.randint(low=5, high=10, size=()) for x in shape])

def build_graph(parameters):
    """Build the sign op testing graph."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])
    num_lower = tf.compat.v1.placeholder(
        dtype=parameters["index_dtype"], name="num_lower", shape=())
    num_upper = tf.compat.v1.placeholder(
        dtype=parameters["index_dtype"], name="num_upper", shape=())
    out = tf.linalg.band_part(input_tensor, num_lower, num_upper)
    exit(([input_tensor, num_lower, num_upper], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    static_input_shape = get_static_shape(parameters["input_shape"])
    input_value = create_tensor_data(parameters["input_dtype"],
                                     static_input_shape)
    num_lower = create_tensor_data(
        parameters["index_dtype"],
        shape=(),
        min_value=-1,
        max_value=static_input_shape[-2])
    num_upper = create_tensor_data(
        parameters["index_dtype"],
        shape=(),
        min_value=-1,
        max_value=static_input_shape[-1])
    exit(([input_value, num_lower, num_upper
           ], sess.run(outputs,
                       dict(zip(inputs, [input_value, num_lower, num_upper])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
