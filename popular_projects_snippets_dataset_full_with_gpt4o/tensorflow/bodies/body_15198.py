# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Create a shape from row_partitions.

    Args:
      row_partitions: a nonempty list of RowPartition objects.
      dtype: the dtype to use, or None to use the row_partitions dtype.

    Returns:
      a DynamicRaggedShape with inner_rank==1.
    """
if not row_partitions:
    raise ValueError("row_partitions cannot be empty")
inner_shape = [row_partitions[-1].nvals()]
exit(DynamicRaggedShape(row_partitions, inner_shape, dtype=dtype))
