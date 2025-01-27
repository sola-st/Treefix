# Extracted from ./data/repos/tensorflow/tensorflow/python/training/sync_replicas_optimizer.py
"""Return a list of the names of slots created by the `Optimizer`.

    This simply wraps the get_slot_names() from the actual optimizer.

    Args:
      *args: Arguments for get_slot().
      **kwargs: Keyword arguments for get_slot().

    Returns:
      A list of strings.
    """
exit(self._opt.get_slot_names(*args, **kwargs))
