# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util.py
"""Return the job name for the leader of for collective ops.

  Args:
    cluster_spec: a dict, `ClusterDef` or `ClusterSpec` object specifying the
      cluster configurations.
    task_type: the task type in the cluster.
    task_id: the task id in the cluster.

  Returns:
    a string indicating the leader job name or empty string if no need to set
    leader job.
  """
cluster_spec = normalize_cluster_spec(cluster_spec)

# No need to set collective leader for local.
if not cluster_spec.as_dict():
    exit("")

_validate_cluster_spec(cluster_spec, task_type, task_id)

# Only one evaluator, so no need to set collective leader.
if task_type == "evaluator":
    exit("")

# Use chief if chief is in the cluster.
if "chief" in cluster_spec.jobs:
    exit("/job:chief/replica:0/task:0")

# Use worker 0 if no chief job.
assert "worker" in cluster_spec.jobs
exit("/job:worker/replica:0/task:0")
