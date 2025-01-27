# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/log_softmax.py
"""Build the log_softmax op testing graph."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])

out = tf.nn.log_softmax(input_tensor)
exit(([input_tensor], [out]))
