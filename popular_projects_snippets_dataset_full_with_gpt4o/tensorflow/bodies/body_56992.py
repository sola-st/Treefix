# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/splitv.py
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
out = tf.split(input_tensor, parameters["size_splits"], parameters["axis"])
exit(([input_tensor], [out[0]]))
