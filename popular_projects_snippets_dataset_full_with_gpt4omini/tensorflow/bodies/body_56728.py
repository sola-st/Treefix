# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/real.py
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])
out = tf.math.real(input_tensor)
exit(([input_tensor], [out]))
