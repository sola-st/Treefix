# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/partitioned_variables.py
"""Partitioner that partitions shards to have max_shard_bytes total size.

    Args:
      shape: A `TensorShape`.
      dtype: A `DType`.

    Returns:
      A tuple representing how much to slice each axis in shape.

    Raises:
      ValueError: If shape is not a fully defined `TensorShape` or dtype is not
        a `DType`.
    """
if not isinstance(shape, tensor_shape.TensorShape):
    raise ValueError(f"shape is not a TensorShape: {shape}")
if not shape.is_fully_defined():
    raise ValueError(f"shape is not fully defined: {shape}")
if not isinstance(dtype, dtypes.DType):
    raise ValueError(f"dtype is not a DType: {dtype}")

if dtype.base_dtype == dtypes.string:
    element_size = bytes_per_string_element
else:
    element_size = dtype.size

partitions = [1] * shape.ndims
bytes_per_slice = 1.0 * (
    shape.num_elements() / shape.dims[axis].value) * element_size
# How many slices can we fit on one shard of size at most max_shard_bytes?
# At least one slice is required.
slices_per_shard = max(1, math.floor(max_shard_bytes / bytes_per_slice))
# How many shards do we need for axis given that each shard fits
# slices_per_shard slices from a total of shape[axis] slices?
axis_shards = int(math.ceil(
    1.0 * shape.dims[axis].value / slices_per_shard))
if max_shards:
    axis_shards = min(max_shards, axis_shards)

partitions[axis] = axis_shards

exit(partitions)
