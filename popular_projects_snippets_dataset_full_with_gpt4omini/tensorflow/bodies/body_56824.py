# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/range.py
"""Build the range op testing graph."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], name=("start"), shape=[])
if parameters["delta"] < 0:
    offset = parameters["offset"] * -1
else:
    offset = parameters["offset"]
delta = parameters["delta"]
limit_tensor = input_tensor + offset
delta_tensor = tf.constant(delta, dtype=parameters["dtype"])
out = tf.range(input_tensor, limit_tensor, delta_tensor)
exit(([input_tensor], [out]))
