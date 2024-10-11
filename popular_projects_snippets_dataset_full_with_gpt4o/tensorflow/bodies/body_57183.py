# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/squeeze.py
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])
out = tf.squeeze(input_tensor, axis=parameters["axis"])
exit(([input_tensor], [out]))
