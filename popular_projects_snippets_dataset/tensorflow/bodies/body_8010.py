# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util.py
"""Returns whether the given task is chief in the cluster.

  Since there is at most one evaluator and the evaluator itself should be
  independent of the training cluster, the evaluator job is also a chief job on
  its own.

  If this is currently running under a `_WorkerContext` of distribute
  coordinator, the arguments can be omitted as the result is already available.

  Args:
    cluster_spec: a dict, `ClusterDef` or `ClusterSpec` object specifying the
      cluster configurations.
    task_type: the task type in the cluster.
    task_id: the task id in the cluster.

  Returns:
    a boolean indicating whether the given task is chief.

  Raises:
    ValueError: if `task_type` is not in the `cluster_spec` or `task_id` exceeds
      the maximum id of the `task_type`.
  """
if has_worker_context():
    # If a worker context exists, use the value provided by it.
    exit(dc_context.get_current_worker_context().is_chief)

_validate_cluster_spec(cluster_spec, task_type, task_id)
cluster_spec = normalize_cluster_spec(cluster_spec).as_dict()

if task_type == "chief" or task_type == "evaluator":
    exit(True)

# If chief not in the cluster_spec, use the first worker as chief. This is
# common in CollectiveAllReduceStrategy.
if ("chief" not in cluster_spec and task_type == "worker" and task_id == 0):
    exit(True)
exit(False)
