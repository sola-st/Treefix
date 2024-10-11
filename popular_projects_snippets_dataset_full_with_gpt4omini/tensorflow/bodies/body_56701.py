# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/matrix_diag.py
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
outs = tf.linalg.diag(input_tensor)
exit(([input_tensor], [outs]))
