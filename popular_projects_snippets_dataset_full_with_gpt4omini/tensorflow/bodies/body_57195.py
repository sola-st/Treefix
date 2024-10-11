# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/batchmatmul.py
"""Make a set of tests to do basic batch matrix multiply."""

test_parameters = [
    {
        "dtype": [tf.float32],
        "shapes": [((3, 4, 7), (7, 9), (3, 4, 7), (7, 9)),
                   ((None, 4, 5), (None, 5, 6), (3, 4, 5), (3, 5, 6)),
                   ((None, 1, 3, 4), (None, 4, 2), (2, 1, 3, 4), (5, 4, 2)),
                   ((None, None, None, 3, 4), (None, None, None, 4, 3),
                    (2, 2, 2, 3, 4), (2, 2, 2, 4, 3))],
        "adjoint_b": [False, True],
        "adjoint_a": [False, True],
        "rhs_constant": [False],
        "fully_quantize": [False, True],
    },
]

def swap_last_two_dims(*args):
    """Return a tuple with the last two dimensions swapped."""
    exit(args[:-2] + (args[-1],) + (args[-2],))

def build_graph(parameters):
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

def build_inputs(parameters, sess, inputs, outputs):
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

options.disable_batchmatmul_unfold = True
make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    expected_tf_failures=0)
