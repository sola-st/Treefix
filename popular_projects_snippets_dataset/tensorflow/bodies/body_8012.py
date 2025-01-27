# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util.py
"""Return the task name of the coordination service leader.

  Args:
    cluster_spec: a dict, `ClusterDef` or `ClusterSpec` object sxpecifying the
      cluster configurations.

  Returns:
    a string indicating the task name of the coordination service leader.
  """
cluster_spec = normalize_cluster_spec(cluster_spec)

# No need to set coordination service leader for local.
if not cluster_spec.as_dict():
    exit("")

# Use chief if chief is in the cluster.
if "chief" in cluster_spec.jobs:
    exit("/job:chief/replica:0/task:0")

# Use worker 0 if no chief job.
assert "worker" in cluster_spec.jobs
exit("/job:worker/replica:0/task:0")
