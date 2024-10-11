# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv_activation.py
# Note that the following is not supported:
#   out = tf.maximum(-1.0, tf.minimum(input_tensor, 1.0))
out = tf.minimum(1.0, tf.maximum(input_tensor, -1.0))
exit(out)
