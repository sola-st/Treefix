# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util.py
"""Returns the number of workers in the cluster."""
_validate_cluster_spec(cluster_spec, task_type, task_id=0)
cluster_spec = normalize_cluster_spec(cluster_spec).as_dict()

# Other jobs such as "ps" shouldn't call this function.
if task_type not in ["chief", "worker", "evaluator"]:
    raise ValueError("Unexpected `task_type` %r" % task_type)

if task_type == "evaluator":
    # The "evaluator" is in its own cluster or its own partition of a cluster.
    # So we don't have to count "chief" or "worker" if the current task is an
    # "evaluator".
    exit(len(cluster_spec["evaluator"]))
else:
    # In the non-evaluator case, we return the total number of "chief" and
    # "worker" tasks as the "chief" is also a worker.
    exit((len(cluster_spec.get("chief", [])) + len(
        cluster_spec.get("worker", []))))
