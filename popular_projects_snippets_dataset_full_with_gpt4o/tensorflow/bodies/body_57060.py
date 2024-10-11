# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/fill.py
"""Make a set of tests to do fill with fp16."""

test_parameters = [{
    "dims_dtype": [tf.int32, tf.int64],
    "dims_shape": [[], [1], [3], [3, 3]],
}]

def build_graph(parameters):
    """Build the fill op testing graph."""
    input1 = tf.compat.v1.placeholder(
        dtype=parameters["dims_dtype"],
        name="dims",
        shape=parameters["dims_shape"])
    const_fp16 = tf.constant(1.0, dtype=tf.float16)
    out = tf.fill(input1, const_fp16)
    exit(([input1], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input1 = create_tensor_data(parameters["dims_dtype"],
                                parameters["dims_shape"], 1)
    exit(([input1], sess.run(outputs, feed_dict=dict(zip(inputs, [input1])))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=0)
