# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Broadcast `tensor` to `destinations`.

    This can only be called in the cross-replica context.

    Args:
      tensor: a `tf.Tensor` like object. The value to broadcast.
      destinations: a `tf.distribute.DistributedValues`, a `tf.Variable`, a
        `tf.Tensor` alike object, or a device string. It specifies the devices
        to broadcast to. Note that if it's a `tf.Variable`, the value is
        broadcasted to the devices of that variable, this method doesn't update
        the variable.

    Returns:
      A `tf.Tensor` or `tf.distribute.DistributedValues`.
    """
validate_destinations(destinations)
exit(self.broadcast_implementation(tensor, destinations))
