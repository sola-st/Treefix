# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/partitioned_variables.py
"""Partitioner to allocate minimum size per slice.

  Returns a partitioner that partitions the variable of given shape and dtype
  such that each partition has a minimum of `min_slice_size` slice of the
  variable. The maximum number of such partitions (upper bound) is given by
  `max_partitions`.

  Args:
    max_partitions: Upper bound on the number of partitions. Defaults to 1.
    axis: Axis along which to partition the variable. Defaults to 0.
    min_slice_size: Minimum size of the variable slice per partition. Defaults
      to 256K.
    bytes_per_string_element: If the `Variable` is of type string, this provides
      an estimate of how large each scalar in the `Variable` is.

  Returns:
    A partition function usable as the `partitioner` argument to
    `variable_scope` and `get_variable`.

  """
def _partitioner(shape, dtype):
    """Partitioner that partitions list for a variable of given shape and type.

    Ex: Consider partitioning a variable of type float32 with
      shape=[1024, 1024].
      If `max_partitions` >= 16, this function would return
        [(1024 * 1024 * 4) / (256 * 1024), 1] = [16, 1].
      If `max_partitions` < 16, this function would return
        [`max_partitions`, 1].

    Args:
      shape: Shape of the variable.
      dtype: Type of the variable.

    Returns:
      List of partitions for each axis (currently only one axis can be
      partitioned).

    Raises:
      ValueError: If axis to partition along does not exist for the variable.
    """
    if axis >= len(shape):
        raise ValueError(
            f"Cannot partition variable along axis {axis} when shape is "
            f"only {shape}")
    if dtype.base_dtype == dtypes.string:
        bytes_per_element = bytes_per_string_element
    else:
        bytes_per_element = dtype.size
    total_size_bytes = shape.num_elements() * bytes_per_element
    partitions = total_size_bytes / min_slice_size
    partitions_list = [1] * len(shape)
    # We can not partition the variable beyond what its shape or
    # `max_partitions` allows.
    partitions_list[axis] = max(1, min(shape.dims[axis].value,
                                       max_partitions,
                                       int(math.ceil(partitions))))
    exit(partitions_list)
exit(_partitioner)
