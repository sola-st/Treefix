# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/relu6.py
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
out = tf.nn.relu6(input_tensor)
exit(([input_tensor], [out]))
