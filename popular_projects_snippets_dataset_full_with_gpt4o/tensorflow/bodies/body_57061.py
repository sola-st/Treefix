# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/matrix_set_diag.py
input_shape = parameters["input_diag_shapes"][0]
diag_shape = parameters["input_diag_shapes"][1]
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"], name="input", shape=input_shape)
diag_tensor = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"], name="diagonal", shape=diag_shape)
outs = tf.linalg.set_diag(input_tensor, diag_tensor)
exit(([input_tensor, diag_tensor], [outs]))
