# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_max_pool_op_test.py
"""Test when there's repeating value in pooling region.

    There's no formal definition for what the gradient should be when there're
    multiple max value within a pooling cell. Such as
        | 1 5 |
        | 5 3 |
    The expected result depends heavily on implementation, if someone swap the
    order of a nested for loop when walking through the tensor, result would be
    very different.

    The goal of this test is to alert when someone else change the
    implementation. Current implementation scans row-by-row.
    """
input_data = [5.0, 4.0, 6.0, 7.0,
              3.0, 5.0, 9.0, 6.0,
              8.0, 8.0, 9.0, 5.0,
              7.0, 4.0, 0.0, 0.0]  # pyformat: disable
input_size = [1, 4, 4, 1]
output_backprop = [12.0, 15.0,
                   17.0, -5.0,
                   6.0, 21.0]  # pyformat: disable
row_seq = [0, 1, 3, 4]
col_seq = [0, 2, 4]
output_data_not_overlapping = [5.0, 7.0,
                               8.0, 9.0,
                               7.0, 0.0]  # pyformat: disable
output_data_overlapping = [9.0, 9.0,
                           9.0, 9.0,
                           7.0, 0.0]  # pyformat: disable
output_size = [1, 3, 2, 1]
expected_input_backprop_not_overlapping = np.reshape(
    [12.0, 0.0, 0.0, 15.0,
     0.0, 0.0, -5.0, 0.0,
     17.0, 0.0, 0.0, 0.0,
     6.0, 0.0, 21.0, 0.0],
    input_size)  # pyformat: disable
expected_input_backprop_overlapping = np.reshape(
    [0.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 39.0, 0.0,
     0.0, 0.0, 0.0, 0.0,
     6.0, 0.0, 21.0, 0.0],
    input_size)  # pyformat: disable
with self.cached_session() as _:
    # Test when overlapping is False
    input_tensor = constant_op.constant(input_data, shape=input_size)
    output_tensor = constant_op.constant(
        output_data_not_overlapping, shape=output_size)
    grad = constant_op.constant(output_backprop, shape=output_size)
    r = gen_nn_ops.fractional_max_pool_grad(
        input_tensor,
        output_tensor,
        grad,
        row_seq,
        col_seq,
        overlapping=False)
    input_backprop_not_overlapping = self.evaluate(r)
    self.assertShapeEqual(
        np.reshape(expected_input_backprop_not_overlapping, input_size), r)
    self.assertAllClose(expected_input_backprop_not_overlapping,
                        input_backprop_not_overlapping)
    # Test when overlapping is True
    output_tensor = constant_op.constant(
        output_data_overlapping, shape=output_size)
    r = gen_nn_ops.fractional_max_pool_grad(
        input_tensor, output_tensor, grad, row_seq, col_seq, overlapping=True)
    input_backprop_overlapping = self.evaluate(r)
    self.assertShapeEqual(
        np.reshape(expected_input_backprop_overlapping, input_size), r)
    self.assertAllClose(expected_input_backprop_overlapping,
                        input_backprop_overlapping)
