# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""All-gather a dense tensor.

    Args:
      input_tensor: a dense tensor. It must have the same shape on all replicas.
      options: an optional tf.distribute.experimental.CommunicationOptions. If
        provided, it overrides the default options.

    Returns:
      The reduced tensor.
    """
instance_key = self._next_instance_key()
options = self._options.merge(options)
ordering_token = self._get_ordering_token()
with ops.device(self._device):
    exit(collective_ops.all_gather_v2(
        input_tensor,
        self._group_size,
        self._group_key,
        instance_key,
        communication_hint=options.implementation.value,
        timeout=options.timeout_seconds,
        ordering_token=ordering_token))
