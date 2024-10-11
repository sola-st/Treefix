# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/space_to_batch_nd.py
"""Build a space_to_batch graph given `parameters`."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])
input_tensors = [input_tensor]

# Get block_shape either as a const or as a placeholder (tensor).
if parameters["constant_block_shape"]:
    block_shape = parameters["block_shape"]
else:
    shape = [len(parameters["block_shape"])]
    block_shape = tf.compat.v1.placeholder(
        dtype=tf.int32, name="shape", shape=shape)
    input_tensors.append(block_shape)

# Get paddings either as a const or as a placeholder (tensor).
if parameters["constant_paddings"]:
    paddings = parameters["paddings"]
else:
    shape = [len(parameters["paddings"]), 2]
    paddings = tf.compat.v1.placeholder(
        dtype=tf.int32, name="paddings", shape=shape)
    input_tensors.append(paddings)

out = tf.space_to_batch(input_tensor, block_shape, paddings)
exit((input_tensors, [out]))
