# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Return the offset of each value.

    RowPartition takes an array x and converts it into sublists.
    offsets[i] is the index of x[i] in its sublist.
    Given a shape, such as:
    [*,*,*],[*,*],[],[*,*]
    This returns:
    0,1,2,0,1,0,1

    Returns:
      an offset for every value.
    """
exit(gen_ragged_math_ops.ragged_range(
    starts=constant_op.constant(0, self.dtype),
    limits=self.row_lengths(),
    deltas=constant_op.constant(1, self.dtype)).rt_dense_values)
