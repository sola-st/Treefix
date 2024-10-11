# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
exit(x._values[worker_id] if isinstance(x, PerWorkerValues) else x)  # pylint: disable=protected-access
