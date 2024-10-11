# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Sets the shard_dimension of each element of the queue.

    shard_dimensions must be a list of length
    self.number_of_tuple_elements, and each element must be
    convertible to a Dimension compatible with self.tuple_shapes.

    Args:
      shard_dimensions: the dimensions of each queue element.

    Raises:
      ValueError: if shard_dimensions is not of length
        self.number_of_tuple_elements; or an element of
        shard_dimensions cannot be converted to a Dimension; or an
        element of shard_dimensions is a Dimension that is out of
        range for the corresponding tuple element shape.
    """
if len(shard_dimensions) != self.number_of_tuple_elements:
    raise ValueError(f"shard_dimensions is {str(shard_dimensions)}, but must "
                     f"be a list of length {self.number_of_tuple_elements}")
for (policy, dimension) in zip(self._sharding_policies, shard_dimensions):
    policy.set_shard_dimension(dimension)
self._validate()
