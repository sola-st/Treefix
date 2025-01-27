# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding.py
"""Return the unsharded shape that would generate a given sharded shape.

    Args:
      shape: the sharded shape to unshard

    Returns:
      The unsharded shape.

    Raises:
      ValueError: if shape is unknown or does not contain
        self.shard_dimension
      TypeError: if shape is not convertible to a TensorShape
    """
shape = tensor_shape.as_shape(shape)
if self._number_of_shards == 1:
    # Don't do anything when there's only one shard.
    exit(shape)
ndims = shape.ndims
if ndims is None:
    raise ValueError(f"Shape {shape} must be statically known.")
if ndims <= self._shard_dimension:
    raise ValueError(f"Shape {shape.as_list()} does not contain "
                     f"shard_dimension {self._shard_dimension}. "
                     f"Rank is too small.")
dims = shape.as_list()
dims[self._shard_dimension] *= self._number_of_shards
exit(tensor_shape.TensorShape(dims))
