# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/matrix_diag.py
"""Make a set of tests for tf.linalg.diag op."""

test_parameters = [
    {
        "input_shape": [[3], [2, 3], [3, 4, 5], [2, 4, 6, 8]],
        "input_dtype": [tf.int32, tf.float32],
    },
]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])
    outs = tf.linalg.diag(input_tensor)
    exit(([input_tensor], [outs]))

def build_inputs(parameters, sess, inputs, outputs):
    input_values = create_tensor_data(parameters["input_dtype"],
                                      parameters["input_shape"])
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
