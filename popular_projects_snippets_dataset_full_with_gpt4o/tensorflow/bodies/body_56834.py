# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/tanh.py
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
out = tf.nn.tanh(input_tensor)
exit(([input_tensor], [out]))
