# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/matrix_band_part.py
"""Build the sign op testing graph."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
num_lower = tf.compat.v1.placeholder(
    dtype=parameters["index_dtype"], name="num_lower", shape=())
num_upper = tf.compat.v1.placeholder(
    dtype=parameters["index_dtype"], name="num_upper", shape=())
out = tf.linalg.band_part(input_tensor, num_lower, num_upper)
exit(([input_tensor, num_lower, num_upper], [out]))
