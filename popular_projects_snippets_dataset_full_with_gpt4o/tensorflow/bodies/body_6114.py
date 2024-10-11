# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Implementation of `broadcast`.

    Args:
      tensor: a `tf.Tensor` like object. The value to broadcast.
      destinations: a `tf.distribute.DistributedValues`, a `tf.Variable`, a
        `tf.Tensor` alike object, or a device string. It specifies the devices
        to broadcast to.
        `destinations`. Note that if it's a `tf.Variable`, the value is
        broadcasted to the devices of that variable, this method doesn't update
        the variable.

    Returns:
      A `tf.Tensor` or `tf.distribute.DistributedValues`.
    """
exit(simple_broadcast(
    tensor,
    destinations,
    always_mirrored=True,
    canonicalize_devices=self._canonicalize_devices))
