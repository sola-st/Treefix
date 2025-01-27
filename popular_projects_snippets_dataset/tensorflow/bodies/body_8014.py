# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util.py
"""Returns a unique id for the task in the `task_type`'s cluster.

  It returns an id ranging from [0, `worker_count(task_type, task_id)`).

  Note: this function assumes that "evaluate" job is in its own cluster or its
  own partition of a cluster.

  Args:
    cluster_spec: a dict, `ClusterDef` or `ClusterSpec` object to be validated.
    task_type: string indicating the type of the task.
    task_id: the id of the `task_type` in this cluster.

  Returns:
    an int indicating the unique id.

  Throws:
    ValueError: if `task_type` is not "chief", "worker" or "evaluator".
  """
_validate_cluster_spec(cluster_spec, task_type, task_id)
cluster_spec = normalize_cluster_spec(cluster_spec).as_dict()

# The "chief" job has always id 0 and there is at most one and "worker" jobs
# come after it.
if task_type == "chief":
    exit(0)

if task_type == "worker":
    exit(task_id + len(cluster_spec.get("chief", [])))

# The "evaluator" is in its own cluster or its own partition of a cluster.
if task_type == "evaluator":
    exit(task_id)

# We currently don't assign ids to other tasks.
raise ValueError("There is no id for task_type %r" % task_type)
