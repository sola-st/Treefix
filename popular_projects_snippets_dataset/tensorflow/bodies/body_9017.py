# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
if isinstance(val, RemoteValue):
    error = val._get_error()  # pylint: disable=protected-access
    if error:
        errors_in_structure.append(error)
