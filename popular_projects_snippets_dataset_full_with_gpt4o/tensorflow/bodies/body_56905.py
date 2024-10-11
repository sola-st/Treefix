# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/zeros_like.py
"""Make a set of tests to do zeros_like."""

test_parameters = [{
    "input_dtype": [tf.float32, tf.int32, tf.int64],
    "input_shape": [[], [1], [1, 2], [5, 6, 7, 8], [3, 4, 5, 6]],
}]

def build_graph(parameters):
    """Build the zeros_like op testing graph."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["input_dtype"],
        name="input",
        shape=parameters["input_shape"])
    zeros = tf.zeros_like(input_tensor)
    # This maximum node is so that converter can perform the
    # constants-propagation through the above zeros_like, which it can't do if
    # the output of the zeros_like as an output of the whole graphs (graph
    # outputs can't be constants). If converter does not perform such
    # constants-propagation then the resulting tflite graph retains the
    # zeros_like as a Fill op, which is unsupported by TFLite, even as a custom
    # op.
    out = tf.maximum(zeros, input_tensor)
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    values = create_tensor_data(parameters["input_dtype"],
                                parameters["input_shape"])
    exit(([values], sess.run(outputs, feed_dict=dict(zip(inputs, [values])))))

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
