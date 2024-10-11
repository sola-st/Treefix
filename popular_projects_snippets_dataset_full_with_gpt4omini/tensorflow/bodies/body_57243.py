# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/squeeze_transpose.py
"""Make a set of tests to do squeeze followed by transpose."""

test_parameters = [{
    "dtype": [tf.int32, tf.float32, tf.int64],
    "input_shape": [[1, 4, 10, 1]],
    "axis": [[-1], [3]],
}]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"],
        name="input",
        shape=parameters["input_shape"])
    out = tf.squeeze(input_tensor, axis=parameters["axis"])
    out = tf.transpose(a=out, perm=[1, 2])
    exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_values = create_tensor_data(parameters["dtype"],
                                      parameters["input_shape"])
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=0)
