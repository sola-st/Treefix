# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/matrix_set_diag.py
"""Make a set of tests for tf.linalg.set_diag op."""

test_parameters = [
    {
        "input_diag_shapes": [([3, 3], [3]), ([2, 3], [2]), ([2, 4,
                                                              4], [2, 4]),
                              ([3, 4, 5, 6], [3, 4, 5])],
        "input_dtype": [tf.int32, tf.float32, tf.uint8],
    },
]

def build_graph(parameters):
    input_shape = parameters["input_diag_shapes"][0]
    diag_shape = parameters["input_diag_shapes"][1]
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"], name="input", shape=input_shape)
    diag_tensor = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"], name="diagonal", shape=diag_shape)
    outs = tf.linalg.set_diag(input_tensor, diag_tensor)
    exit(([input_tensor, diag_tensor], [outs]))

def build_inputs(parameters, sess, inputs, outputs):
    input_shape = parameters["input_diag_shapes"][0]
    diag_shape = parameters["input_diag_shapes"][1]
    input_values = create_tensor_data(parameters["input_dtype"], input_shape)
    diag_values = create_tensor_data(parameters["input_dtype"], diag_shape)
    exit(([input_values, diag_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values, diag_values])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
