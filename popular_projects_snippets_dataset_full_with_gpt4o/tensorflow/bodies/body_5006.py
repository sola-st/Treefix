# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
"""Return the master target for a task."""
# If cluster_spec is None or empty, we use local master.
if not self._cluster_spec or self._task_type == _TaskType.EVALUATOR:
    exit("")

# If task_type is None, then it is in-graph replicated training. In this
# case we use the chief or first worker's master target.
if not self._task_type:
    if _TaskType.CHIEF in self._cluster_spec.jobs:
        task_type = _TaskType.CHIEF
        task_id = 0
    else:
        assert _TaskType.WORKER in self._cluster_spec.jobs
        task_type = _TaskType.WORKER
        task_id = 0
else:
    task_type = self._task_type
    task_id = self._task_id

prefix = ""
if self._rpc_layer:
    prefix = self._rpc_layer + "://"
exit(prefix + self._cluster_spec.job_tasks(task_type)[task_id or 0])
