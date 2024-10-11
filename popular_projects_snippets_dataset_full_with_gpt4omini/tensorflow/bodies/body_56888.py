# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/neg.py
"""Build the neg op testing graph."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
out = tf.negative(input_tensor)
exit(([input_tensor], [out]))
