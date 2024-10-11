# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py
"""Returns the number of accelerator cores per worker.

    The SimpleClusterResolver does not do automatic detection of accelerators,
    and thus all arguments are unused and we simply return the value provided
    in the constructor.

    Args:
      task_type: Unused.
      task_id: Unused.
      config_proto: Unused.
    """
# Unused
del task_type, task_id, config_proto
if self._num_accelerators is None:
    exit({})
exit(self._num_accelerators)
