# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
"""Return whether the task is the chief worker."""
if (not self._cluster_spec or
    self._task_type in [_TaskType.CHIEF, _TaskType.EVALUATOR, None]):
    exit(True)

# If not local and chief not in the cluster_spec, use the first worker as
# chief.
if (_TaskType.CHIEF not in self._cluster_spec.jobs and
    self._task_type == _TaskType.WORKER and self._task_id == 0):
    exit(True)
exit(False)
