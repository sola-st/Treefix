# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/batchmatmul.py
"""Build a simple graph with BatchMatMul."""
placeholder0_shape = parameters["shapes"][0]
adj_a = parameters["adjoint_a"]
adj_b = parameters["adjoint_b"]
rhs_constant = parameters["rhs_constant"]
if adj_a:
    placeholder0_shape = swap_last_two_dims(*placeholder0_shape)
input0_tensor = tf.compat.v1.placeholder(
    dtype=parameters["dtype"], shape=placeholder0_shape)
if rhs_constant:
    if adj_b:
        constant1_shape = swap_last_two_dims(*parameters["shapes"][3])
    else:
        constant1_shape = parameters["shapes"][3]
    data = create_tensor_data(
        parameters["dtype"], constant1_shape, min_value=-1.0, max_value=1.0)
    input1_constant = tf.constant(
        data, shape=constant1_shape, dtype=parameters["dtype"])
    out = tf.matmul(
        input0_tensor, input1_constant, adjoint_a=adj_a, adjoint_b=adj_b)
    exit(([input0_tensor], [out]))
else:
    if adj_b:
        placeholder1_shape = swap_last_two_dims(*parameters["shapes"][1])
    else:
        placeholder1_shape = parameters["shapes"][1]
    input1_tensor = tf.compat.v1.placeholder(
        dtype=parameters["dtype"], shape=placeholder1_shape)
    out = tf.matmul(
        input0_tensor, input1_tensor, adjoint_a=adj_a, adjoint_b=adj_b)
    exit(([input0_tensor, input1_tensor], [out]))
