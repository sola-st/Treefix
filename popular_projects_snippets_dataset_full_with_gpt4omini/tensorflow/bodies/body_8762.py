# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/coordinator_context.py
e = (
    cluster_coordinator._maybe_rebuild_remote_values(  # pylint: disable=protected-access
        self._worker, remote_value))
if e:
    if not isinstance(e, cluster_coordinator.ClosureInputError):
        e = cluster_coordinator.ClosureInputError(e)
    raise e
