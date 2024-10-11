# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/space_to_depth.py
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])
out = tf.compat.v1.space_to_depth(
    input=input_tensor, block_size=parameters["block_size"])
exit(([input_tensor], [out]))
