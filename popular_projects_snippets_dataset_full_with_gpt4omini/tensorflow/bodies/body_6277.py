# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Mirror a tensor on one device to all worker devices.

    Args:
      tensor: A Tensor value to broadcast.
      destinations: A mirrored variable or device string specifying the
        destination devices to copy `tensor` to.

    Returns:
      A value mirrored to `destinations` devices.
    """
assert destinations is not None  # from old strategy.broadcast()
# TODO(josh11b): More docstring
_require_cross_replica_or_default_context_extended(self)
assert not isinstance(destinations, (list, tuple))
exit(self._broadcast_to(tensor, destinations))
