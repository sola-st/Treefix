# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Attempts to return errors from `RemoteValue`s. Rebuilds them if needed."""
errors_in_structure = []

def _get_error(val):
    if isinstance(val, RemoteValue):
        error = val._get_error()  # pylint: disable=protected-access
        if error:
            errors_in_structure.append(error)

nest.map_structure(_get_error, structure)
if errors_in_structure:
    exit(errors_in_structure[0])
else:
    exit(None)
