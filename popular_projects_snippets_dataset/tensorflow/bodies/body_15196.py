# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Core constructor for a DynamicRaggedShape.

    Create a DynamicRaggedShape. This can be used to construct a
    DynamicRaggedShape representing a ragged or dense shape. If row_partitions
    is an empty list, then this is equivalent to a dense shape.

    If row_partitions is specified, then the num_row_partitions will be equal
    to len(row_partitions). There are several checks made.
    Specifically:
    1. Consecutive row_partitions must have consistent nvals and nrows.
    2. The last row_partitions must have nvals equal to the first element of
       inner_shape.

    The inner_shape is converted to a tensor.
    All row_partitions and the inner_shape are converted to the same dtype
    (int64 or int32).

    Args:
      row_partitions: the row_partitions of the shape.
      inner_shape: if len(row_partitions) > 0, the shape of the flat_values.
        Otherwise, the shape of the tensor.
      dtype: tf.int64, tf.int32, or None representing the preferred dtype.
      validate: if true, dynamic validation is applied to the shape.
      static_inner_shape: if len(row_partitions) > 0, the static shape of the
        flat_values. Otherwise, the static shape of the tensor. Should be
        convertible to a TensorShape.
    """
if not isinstance(row_partitions, Iterable):
    raise TypeError(
        "row_partitions should be a list of row partitions. Instead, got " +
        str(row_partitions))
for x in row_partitions:
    if not isinstance(x, RowPartition):
        raise TypeError("row_partitions contains " + str(x) +
                        " which is not a RowPartition")
dtype = _find_dtype_iterable(row_partitions, dtype)
dtype = _find_dtype(inner_shape, dtype)
if (isinstance(inner_shape, np.ndarray) and
    inner_shape.dtype == np.int32 and dtype is None):
    dtype = dtypes.int32
dtype = _find_dtype(dtypes.int64, dtype)

row_partitions = tuple([rp.with_dtype(dtype) for rp in row_partitions])
self._row_partitions = row_partitions
self._inner_shape = ops.convert_to_tensor(
    inner_shape, dtype_hint=dtype, name="inner_dim_sizes")
if self._inner_shape.dtype != dtype:
    self._inner_shape = math_ops.cast(self._inner_shape, dtype)

checks = []
# Validate shapes.
if self._row_partitions:
    for axis, rp in enumerate(self._row_partitions):
        if axis > 0:
            previous_row_partition = self._row_partitions[axis - 1]
            msg = ("RowPartitions in DynamicRaggedShape do not align "
                   f"between {axis - 1} and {axis}")
            static_nrows = rp.static_nrows
            static_nvals = previous_row_partition.static_nvals
            if (static_nrows is not None) and (static_nvals is not None):
                if static_nrows != static_nvals:
                    raise ValueError(msg)
                else:
                    continue
            if validate:
                checks.append(
                    check_ops.assert_equal(
                        previous_row_partition.nvals(), rp.nrows(), message=msg))

self._inner_shape.shape.assert_has_rank(1)

self._static_inner_shape = tensor_util.constant_value_as_shape(
    self._inner_shape)
if static_inner_shape is not None:
    self._static_inner_shape = self._static_inner_shape.merge_with(
        static_inner_shape)

if row_partitions:
    last_row_partition = row_partitions[-1]
    static_nvals = last_row_partition.static_nvals
    static_inner_shape_nvals = tensor_shape.dimension_value(
        self._static_inner_shape[0])
    if static_nvals is not None and static_inner_shape_nvals is not None:
        if static_nvals != static_inner_shape_nvals:
            raise ValueError("Last row partition does not match inner_shape.")
    elif validate:
        checks.append(
            check_ops.assert_equal(
                last_row_partition.nvals(),
                self._inner_shape[0],
                message="Last row partition does not match inner_shape."))
if checks:
    self._inner_shape = control_flow_ops.with_dependencies(
        checks, self._inner_shape, name="inner_shape_validated")
    self._row_partitions = [
        rp._with_dependencies(checks) for rp in self._row_partitions  # pylint: disable=protected-access
    ]
