# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/binary_op.py
"""Builds the graph given the current parameters."""
input1 = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input1",
    shape=parameters["input_shape_1"])
input2 = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input2",
    shape=parameters["input_shape_2"])
out = binary_operator(input1, input2)
if parameters["activation"] and (parameters["dtype"] != tf.int32 and
                                 parameters["dtype"] != tf.int64):
    out = tf.nn.relu(out)
exit(([input1, input2], [out]))
