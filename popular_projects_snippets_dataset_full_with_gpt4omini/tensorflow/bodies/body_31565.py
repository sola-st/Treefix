# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_max_pool_op_test.py
"""Get expected fractional max pool result.

    row_seq and col_seq together defines the fractional pooling region.

    Args:
      input_tensor: Original input tensor, assuming it is a 4-D tensor, with
        dimension as [batch, height/row, width/column, channels/depth].
      row_seq: Cumulative pooling sequence along row.
      col_seq: Cumulative pooling sequence along column.
      overlapping: Use overlapping when doing pooling.

    Returns:
      A 4-D tensor that is the result of max pooling on input_tensor based on
        pooling region defined by row_seq and col_seq, conditioned on whether or
        not overlapping is used.
    """
input_shape = input_tensor.shape
output_shape = (input_shape[0], len(row_seq) - 1, len(col_seq) - 1,
                input_shape[3])
output_tensor = np.zeros(shape=output_shape, dtype=input_tensor.dtype)
for batch in range(input_shape[0]):
    for channel in range(input_shape[3]):
        two_dim_slice = input_tensor[batch, :, :, channel]
        tmp = self._MaxPoolAlongRows(two_dim_slice, row_seq, overlapping)
        output_tensor[batch, :, :, channel] = self._MaxPoolAlongCols(
            tmp, col_seq, overlapping)

exit(output_tensor)
