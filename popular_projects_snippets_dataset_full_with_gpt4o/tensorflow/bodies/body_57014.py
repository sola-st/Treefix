# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/einsum.py
"""Build a simple graph with einsum Op."""
input0_shape = parameters["shapes"][0]
input1_shape = parameters["shapes"][1]
equation = parameters["shapes"][2]

input0_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], shape=input0_shape)
input1_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], shape=input1_shape)
out = tf.einsum(equation, input0_tensor, input1_tensor)
exit(([input0_tensor, input1_tensor], [out]))
