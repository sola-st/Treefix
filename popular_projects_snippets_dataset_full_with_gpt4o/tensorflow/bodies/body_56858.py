# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/elementwise.py
"""Build the unary op testing graph."""
input_value = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input1",
    shape=parameters["input_shape"])
out = op(input_value)
exit(([input_value], [out]))
