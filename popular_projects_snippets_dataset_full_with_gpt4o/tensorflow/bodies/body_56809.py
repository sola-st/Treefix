# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/batch_to_space_nd.py
"""Build a batch_to_space graph given `parameters`."""
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

# Get crops either as a const or as a placeholder (tensor).
if parameters["constant_crops"]:
    crops = parameters["crops"]
else:
    shape = [len(parameters["crops"]), 2]
    crops = tf.compat.v1.placeholder(
        dtype=tf.int32, name="crops", shape=shape)
    input_tensors.append(crops)

out = tf.batch_to_space(input_tensor, block_shape, crops)
exit((input_tensors, [out]))
