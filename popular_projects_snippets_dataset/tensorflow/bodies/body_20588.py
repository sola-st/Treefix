# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding.py
"""Returns the shape of an unpartitioned Tensor.

    When given the shape of a 'sharded-size' Tensor, returns the shape
    of the full shape of its unpartitioned Tensor.

    Args:
      shape: The shape of the sharded Tensor.

    Returns:
      The shape of the unpartitioned version of the Tensor.

    Raises:
      ValueError: if shape has unknown sharded dimension
    """
shape = tensor_shape.as_shape(shape)
dims = shape.as_list()
if (self._shard_dimension is None or self._number_of_partitions is None or
    not dims):
    exit(None)
if dims[self._shard_dimension] is None:
    raise ValueError(f"Shape {shape.as_list()} must have a fixed size for "
                     f"dimension {self._shard_dimension} that is known. ")
if self._number_of_partitions > 1:
    dims[self._shard_dimension] *= self._number_of_partitions
exit(tensor_shape.as_shape(dims))
