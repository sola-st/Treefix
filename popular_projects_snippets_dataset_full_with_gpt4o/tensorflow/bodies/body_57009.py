# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unroll_batch_matmul.py
"""Build the graph."""
input_tensor1 = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], shape=parameters["shape"][0])
input_tensor2 = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], shape=parameters["shape"][1])
# Should be unrolled and replaced with fully_connected ops in the end.
out = tf.matmul(
    input_tensor1,
    input_tensor2,
    transpose_a=parameters["shape"][2],
    transpose_b=parameters["shape"][3])
exit(([input_tensor1, input_tensor2], [out]))
