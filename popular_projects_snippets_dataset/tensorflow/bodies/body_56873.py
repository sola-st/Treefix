# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/fully_connected.py
"""Build a matmul graph given `parameters`."""
input_tensor1 = tf.compat.v1.placeholder(
    dtype=tf.float32, name="input1", shape=parameters["shape1"])

# Get input_tensor2 either as a placeholder or constants. Also get a list of
# the input tensors that are represented as placeholders.
if parameters["constant_filter"]:
    input_tensor2 = create_tensor_data(
        np.float32, parameters["shape2"], min_value=-1, max_value=1)
    input_tensors = [input_tensor1]
else:
    input_tensor2 = tf.compat.v1.placeholder(
        dtype=tf.float32, name="input2", shape=parameters["shape2"])
    input_tensors = [input_tensor1, input_tensor2]

out = tf.matmul(
    input_tensor1,
    input_tensor2,
    transpose_a=parameters["transpose_a"],
    transpose_b=parameters["transpose_b"])
exit((input_tensors, [out]))
