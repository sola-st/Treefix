# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/imag.py
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])
out = tf.math.imag(input_tensor)
exit(([input_tensor], [out]))
