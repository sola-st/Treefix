# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/add_n.py
"""Builds the graph given the current parameters."""
input_tensors = []
for i in range(parameters["num_inputs"]):
    input_tensors.append(
        tf.compat.v1.placeholder(
            dtype=parameters["dtype"],
            name="input_{}".format(i),
            shape=parameters["input_shape"]))
out = tf.add_n(input_tensors)
exit((input_tensors, [out]))
