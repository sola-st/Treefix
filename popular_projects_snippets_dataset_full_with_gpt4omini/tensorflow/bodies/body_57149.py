# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/relu1.py
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
# Note that the following is not supported:
#   out = tf.maximum(-1.0, tf.minimum(input_tensor, 1.0))
out = tf.minimum(1.0, tf.maximum(input_tensor, -1.0))
exit(([input_tensor], [out]))
