# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/mirror_pad.py
"""Build the graph for the test case."""

input_tensor = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input", shape=parameters["input_shape"])
if parameters["type"] != "const" and not parameters["fully_quantize"]:
    padding_matrix = tf.compat.v1.placeholder(
        dtype=tf.int32,
        name="padding",
        shape=[len(parameters["input_shape"]), 2])
    input_tensors = [input_tensor, padding_matrix]
else:
    padding_matrix = tf.constant(np.array(parameters["padding_matrix"]))
    input_tensors = [input_tensor]
output = tf.pad(
    tensor=input_tensor, paddings=padding_matrix, mode=parameters["mode"])

exit((input_tensors, [output]))
