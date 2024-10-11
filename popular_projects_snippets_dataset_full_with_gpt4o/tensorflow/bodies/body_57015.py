# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/einsum.py
"""Feed inputs, assign variables, and freeze graph."""
input0_shape = set_dynamic_shape(parameters["shapes"][0])
input1_shape = set_dynamic_shape(parameters["shapes"][1])
input0_value = create_tensor_data(parameters["dtype"], input0_shape)
input1_value = create_tensor_data(parameters["dtype"], input1_shape)
output_values = sess.run(
    outputs, feed_dict=dict(zip(inputs, [input0_value, input1_value])))
exit(([input0_value, input1_value], output_values))
