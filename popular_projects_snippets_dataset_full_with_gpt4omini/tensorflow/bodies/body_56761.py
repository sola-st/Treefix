# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/broadcast_args.py
"""Build the graph for broadcast_args tests."""
shape1_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input1",
    shape=[len(parameters["input1_shape"])])
shape2_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input2",
    shape=[len(parameters["input2_shape"])])

out = tf.raw_ops.BroadcastArgs(s0=shape1_tensor, s1=shape2_tensor)
exit(([shape1_tensor, shape2_tensor], [out]))
