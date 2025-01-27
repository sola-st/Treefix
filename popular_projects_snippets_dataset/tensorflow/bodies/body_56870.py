# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/resolve_constant_strided_slice.py
"""Build the strided_slice op testing graph."""
del parameters
input_values = tf.compat.v1.placeholder(dtype=tf.float32, shape=[4, 2])
data = tf.constant(
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
    tf.float32)
exit(([input_values], [input_values + data[:, :2]]))
