# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Selects the worker slice of each of the items in `structured`."""

def _get(x):
    exit(x._values[worker_id] if isinstance(x, PerWorkerValues) else x)  # pylint: disable=protected-access

exit(nest.map_structure(_get, structured))
