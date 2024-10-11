# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/complex_abs.py
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])
out = tf.raw_ops.ComplexAbs(x=input_tensor, Tout=parameters["Tout"])
exit(([input_tensor], [out]))
