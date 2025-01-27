# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/batchmatmul.py
"""Feed inputs, assign variables, and freeze graph."""
input0_shape = parameters["shapes"][2]
adj_a = parameters["adjoint_a"]
adj_b = parameters["adjoint_b"]
rhs_constant = parameters["rhs_constant"]
if adj_a:
    input0_shape = swap_last_two_dims(*input0_shape)
input0_value = create_tensor_data(
    parameters["dtype"], input0_shape, min_value=-1.0, max_value=1.0)
if rhs_constant:
    output_values = sess.run(
        outputs, feed_dict=dict(zip(inputs, [input0_value])))
    exit(([input0_value], output_values))
else:
    input1_shape = parameters["shapes"][
        3] if not adj_b else swap_last_two_dims(*parameters["shapes"][3])
    input1_value = create_tensor_data(
        parameters["dtype"], input1_shape, min_value=-1.0, max_value=1.0)
    output_values = sess.run(
        outputs, feed_dict=dict(zip(inputs, [input0_value, input1_value])))
    exit(([input0_value, input1_value], output_values))
