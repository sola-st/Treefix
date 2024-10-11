# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/hardswish.py
inp = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
out = inp * tf.nn.relu6(inp + np.float32(3)) * np.float32(1. / 6.)

exit(([inp], [out]))
