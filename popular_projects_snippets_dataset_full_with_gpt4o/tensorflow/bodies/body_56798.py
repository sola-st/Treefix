# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/depth_to_space.py
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])
out = tf.compat.v1.depth_to_space(
    input_tensor, block_size=parameters["block_size"])
exit(([input_tensor], [out]))
