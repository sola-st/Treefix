# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Checks that the configuration is self-consistent.

    Raises:
      ValueError: if the shapes and sharding policies don't match.
    """
if self.tuple_shapes is not None:
    for (policy, shape) in zip(self._sharding_policies, self._tuple_shapes):
        # Raise an error if the policy is incompatible with the shape.
        _ = policy.get_sharded_shape(shape)
