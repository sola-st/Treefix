# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/relu.py
input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
out = tf.nn.relu(input_tensor)
exit(([input_tensor], [out]))
