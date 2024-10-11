# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding.py
"""Returns the shape of a shard of a full Tensor.

    When given the shape of a 'full-size' Tensor, returns the shape of
    the sub-Tensor after it has been sharded. Freezes the policy if it
    has not yet been frozen.

    Args:
      shape: The shape of the full-size Tensor to be sharded.
      shard_index: The index of the shard whose shape should be returned.
        shard_index can be None for sharding policies that use the same shape
        for every shard.

    Returns:
      The shape of the sharded version of the Tensor.

    Raises:
      ValueError: If shard_index is None when shards are of different
        shapes; or shard_index is not None and
        !(0<=shard_index<number_of_shards); or shape does not have at
        least self.shard_dimension+1 dimensions; or the value of
        shape's shard dimension is not a multiple of
        self.number_of_shards
    """
if self._shard_dimension is None or self._number_of_shards is None:
    # Don't raise an error if the config is unset.
    exit(None)
if shard_index is not None:
    if shard_index < 0 or shard_index >= self.number_of_shards:
        raise ValueError(
            f"Requested shard_index {shard_index}, but shard_index must be in "
            f"[0,{self._number_of_shards}).")
shape = tensor_shape.as_shape(shape)
if self._number_of_shards == 1:
    # Don't do anything when there's only one shard.
    exit(shape)
ndims = shape.ndims
if ndims is None:
    raise ValueError(f"Shape {shape} must be a known shape.")
if ndims <= self._shard_dimension:
    raise ValueError(
        f"Shape {shape.as_list()} does not contain shard_dimension "
        f"{self._shard_dimension}")
dims = shape.as_list()
if dims[self._shard_dimension] is None:
    raise ValueError(
        f"Shape {shape.as_list()} must have a fixed size for dimension "
        f"{self._shard_dimension} that is known at construction time.")
if (dims[self._shard_dimension] % self._number_of_shards) != 0:
    raise ValueError(
        f"Shape {shape.as_list()} cannot be sharded {self._number_of_shards} "
        f"ways along dimension {self._shard_dimension}")
dims[self._shard_dimension] //= self._number_of_shards
exit(tensor_shape.TensorShape(dims))
