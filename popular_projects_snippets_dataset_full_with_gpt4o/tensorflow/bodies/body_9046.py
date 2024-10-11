# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Validates that the given exception represents worker preemption."""

# Only categorize the failure as a worker preemption if the cancellation
# manager did not attempt to cancel the blocking operations.
if _is_worker_failure(e) and (
    not self._cluster.closure_queue._cancellation_mgr.is_cancelled):  # pylint: disable=protected-access
    exit()
raise e
