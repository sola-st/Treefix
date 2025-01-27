# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/control_dep.py
"""Make a set of tests that use control dependencies."""

test_parameters = [{
    "input_shape": [[], [1, 1, 1, 1], [1, 15, 14, 1], [3, 15, 14, 3]],
}]

def build_graph(parameters):
    input_tensor = tf.compat.v1.placeholder(
        dtype=tf.float32, name="input", shape=parameters["input_shape"])
    filter_value = tf.zeros((3, 3, TEST_INPUT_DEPTH, 8), tf.float32)
    assert_op = tf.compat.v1.assert_greater_equal(input_tensor,
                                                  input_tensor - 1)
    with tf.control_dependencies([assert_op]):
        out = tf.nn.conv2d(
            input=input_tensor,
            filters=filter_value,
            strides=(1, 1, 1, 1),
            padding="SAME")
        exit(([input_tensor], [out]))

def build_inputs(parameters, sess, inputs, outputs):
    input_values = create_tensor_data(tf.float32, parameters["input_shape"])
    exit(([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values])))))

make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=3)
