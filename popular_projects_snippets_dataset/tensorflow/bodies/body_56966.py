# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/softmax.py
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])
out = tf.nn.softmax(input_tensor, axis=parameters["dim"])
exit(([input_tensor], [out]))
