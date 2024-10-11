# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Gather `value` across replicas along axis-th dimension to `destinations`.

    `gather_to` gathers `tf.distribute.DistributedValues` or `tf.Tensor`-like
    object, along `axis`-th dimension. It supports only dense tensors but NOT
    sparse tensor. This API can only be called in cross-replica context.

    Args:
      value: a `tf.distribute.DistributedValues`, or a `tf.Tensor` like object.
      destinations: a `tf.distribute.DistributedValues`, a `tf.Variable`, a
        `tf.Tensor` alike object, or a device string. It specifies the devices
        to reduce to. To perform an all-gather, pass the same to `value` and
        `destinations`. Note that if it's a `tf.Variable`, the value is reduced
        to the devices of that variable, and this method doesn't update the
        variable.
      axis: 0-D int32 Tensor. Dimension along which to gather. Must be in the
        range [0, rank(value)).
      options: a `tf.distribute.experimental.CommunicationOptions`. Options to
        perform collective operations. This overrides the default options if the
        `tf.distribute.Strategy` takes one in the constructor. See
        `tf.distribute.experimental.CommunicationOptions` for details of the
        options.

    Returns:
      A tensor or value gathered to `destinations`.
    """
_require_cross_replica_or_default_context_extended(self)
assert not isinstance(destinations, (list, tuple))
if options is None:
    options = collective_util.Options()
exit(self._gather_to_implementation(value, destinations, axis, options))
