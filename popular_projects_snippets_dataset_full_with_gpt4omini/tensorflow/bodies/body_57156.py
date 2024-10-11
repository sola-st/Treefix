# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reverse_v2.py
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name=("input"),
    shape=parameters["base_shape"])
outs = tf.reverse(input_tensor, axis=[get_valid_axis(parameters)])
exit(([input_tensor], [outs]))
