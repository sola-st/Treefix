# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/stft.py
input_value = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    name="input",
    shape=parameters["input_shape"])
outs = tf.signal.stft(
    input_value,
    frame_length=parameters["frame_length"],
    frame_step=parameters["frame_step"],
    fft_length=parameters["fft_length"])
exit(([input_value], [outs]))
