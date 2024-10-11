# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/control_dep.py
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
