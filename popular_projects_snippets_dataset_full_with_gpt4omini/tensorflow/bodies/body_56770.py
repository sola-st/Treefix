# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/pad.py
"""Build a pad graph given `parameters`."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])

# Get paddings as either a placeholder or constants.
if parameters["constant_paddings"]:
    paddings = parameters["paddings"]
    input_tensors = [input_tensor]
else:
    shape = [len(parameters["paddings"]), 2]
    paddings = tf.compat.v1.placeholder(
        dtype=tf.int32, name="padding", shape=shape)
    input_tensors = [input_tensor, paddings]

out = tf.pad(tensor=input_tensor, paddings=paddings)
exit((input_tensors, [out]))
