# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/rfft.py
input_value = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
outs = tf.signal.rfft(input_value, fft_length=parameters["fft_length"])
exit(([input_value], [outs]))
