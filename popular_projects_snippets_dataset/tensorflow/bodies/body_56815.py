# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/sigmoid.py
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])
out = tf.sigmoid(input_tensor)
exit(([input_tensor], [out]))
