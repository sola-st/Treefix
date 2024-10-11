# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reshape.py
"""Build the graph for reshape tests."""
input_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"],
    name="input",
    shape=parameters["input_shape"])

# Get shape as either a placeholder or constants.
if parameters["constant_shape"]:
    output_shape = parameters["output_shape"]
    input_tensors = [input_tensor]
else:
    # The shape of the shape tensor.
    shape_tensor_shape = [len(parameters["output_shape"])]
    output_shape = tf.compat.v1.placeholder(
        dtype=tf.int32, name="output_shape", shape=shape_tensor_shape)
    input_tensors = [input_tensor, output_shape]
out = tf.reshape(input_tensor, shape=output_shape)
exit((input_tensors, [out]))
