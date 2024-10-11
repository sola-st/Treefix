# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/roll.py
input_value = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
outs = tf.roll(
    input_value, shift=parameters["shift"], axis=parameters["axis"])
exit(([input_value], [outs]))
