# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Create a Spec given row partitions, a static inner shape, and a dtype.

      Args:
        row_partitions: A sequence of `RowPartitionSpec`s describing how the
          ragged shape is partitioned.
        static_inner_shape: The static shape of the flat_values.
        dtype: The DType used to encode the shape (tf.int64 or tf.int32).
      """
# Independent validation and coercion of each argument.
if not isinstance(row_partitions, Iterable):
    raise TypeError("row_partitions should be an Iterable")

row_partitions = tuple(row_partitions)

static_inner_shape = tensor_shape.as_shape(static_inner_shape)

dtype = dtypes.as_dtype(dtype)

if not all(isinstance(rp, RowPartitionSpec) for rp in row_partitions):
    raise TypeError(
        "row_partitions should be an Iterable of RowPartitionSpecs")

if dtype != dtypes.int32 and dtype != dtypes.int64:
    raise ValueError("dtype must be tf.int32 or tf.int64")

# All fields are now typechecked and internally consistent.
for spec in row_partitions:
    if spec.dtype != dtype:
        raise ValueError(
            f"dtype of {spec!r} is {spec.dtype!r}: expected {dtype!r}")

row_partitions = tuple(row_partitions)

inner_rank = static_inner_shape.rank

if inner_rank == 0:
    if row_partitions:
        raise ValueError(
            "If row_partitions are provided, must have inner_rank > 0")
else:
    num_slices_in_dimension = []  # type: Sequence[tensor_shape.Dimension]

    # We first attempt to calculate num_slices_in_dimension through a
    # forward pass, using nrows[k] = nrows[k-1] * uniform_row_length
    # and other tricks.
    for i in range(len(row_partitions)):
        rp = row_partitions[i]
        result = tensor_shape.Dimension(rp.nrows)
        if i > 0:
            previous_rp = row_partitions[i - 1]
            result = result.merge_with(previous_rp.nvals)
            result = result.merge_with(num_slices_in_dimension[-1] *
                                       previous_rp.uniform_row_length)
        num_slices_in_dimension.append(result)
    # In the last step of the forward pass,
    # we combine nvals and the first dimension in static_inner_shape.
    if row_partitions:
        last_rp = row_partitions[-1]
        result = (num_slices_in_dimension[-1] *
                  last_rp.uniform_row_length).merge_with(last_rp.nvals)
        if inner_rank is not None:
            result = result.merge_with(
                tensor_shape.dimension_at_index(static_inner_shape, 0))
            static_inner_shape = result + static_inner_shape[1:]
        num_slices_in_dimension.append(result)

    # Now, we start a backward pass.
    for i in range(len(num_slices_in_dimension) - 1, 0, -1):
        num_slices_in_dimension[i - 1] = num_slices_in_dimension[
            i - 1].merge_with(
                _safe_floor_div(num_slices_in_dimension[i],
                                row_partitions[i - 1].uniform_row_length))

    # Finally, we construct the partitions.
    row_partitions = [
        RowPartitionSpec(  # pylint: disable=g-complex-comprehension
            nrows=num_slices_in_dimension[i].value,
            uniform_row_length=rp.uniform_row_length,
            nvals=num_slices_in_dimension[i + 1].value,
            dtype=rp.dtype) for i, rp in enumerate(row_partitions)
    ]

self._static_inner_shape = static_inner_shape
self._inner_shape = tensor_spec.TensorSpec([inner_rank], dtype=dtype)
self._row_partitions = row_partitions
