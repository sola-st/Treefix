# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/add_n.py
"""Builds operand inputs for op."""
input_data = []
for _ in range(parameters["num_inputs"]):
    input_data.append(
        create_tensor_data(parameters["dtype"], parameters["input_shape"]))
exit((input_data, sess.run(
    outputs, feed_dict={i: d for i, d in zip(inputs, input_data)})))
