# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reduce.py
"""Build the mean op testing graph."""
dtype = parameters["input_dtype"]
if boolean_tensor_only:
    dtype = tf.bool
input_tensor = tf.compat.v1.placeholder(
    dtype=dtype, name="input", shape=parameters["input_shape"])

# Get axis as either a placeholder or constants.
if parameters["const_axis"]:
    axis = parameters["axis"]
    input_tensors = [input_tensor]
else:
    if isinstance(parameters["axis"], list):
        shape = [len(parameters["axis"])]
    else:
        shape = []  # shape for None or integers.
    axis = tf.compat.v1.placeholder(
        dtype=tf.int32, name="axis", shape=shape)
    input_tensors = [input_tensor, axis]

out = reduce_op(input_tensor, axis=axis, keepdims=parameters["keepdims"])
exit((input_tensors, [out]))
