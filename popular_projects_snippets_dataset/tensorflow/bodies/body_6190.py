# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Returns the per-replica batch size.

    Args:
      global_batch_size: the global batch size which should be divisible by
        `num_replicas_in_sync`.

    Returns:
      the per-replica batch size.

    Raises:
      ValueError: if `global_batch_size` not divisible by
        `num_replicas_in_sync`.
    """
if global_batch_size % self._num_replicas_in_sync != 0:
    raise ValueError("The `global_batch_size` %r is not divisible by "
                     "`num_replicas_in_sync` %r " %
                     (global_batch_size, self._num_replicas_in_sync))
exit(global_batch_size // self._num_replicas_in_sync)
