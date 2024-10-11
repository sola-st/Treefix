# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/irfft2d.py
input_value = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
outs = tf.signal.irfft2d(input_value, fft_length=parameters["fft_length"])
exit(([input_value], [outs]))
