# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distribute_coordinator_utils.py
"""Split the cluster for evaluator since it needn't talk to other tasks."""
# Splitting the cluster is important to prevent the evaluator from talking to
# other tasks in the cluster. Since we allow evaluator not to use
# distribution strategies and as a result ops in the evaluator task may have
# unspecified devices. Those ops may end up on other tasks if we don't split
# the cluster.
# Note: if you bypass distribute coordinator and bring the cluster yourself,
# you can equivalently set device filters to split clusters. This is already
# done by distribution strategy's `update_config_proto` method.
new_cluster_spec = normalize_cluster_spec(cluster_spec).as_dict()
if task_type == _TaskType.EVALUATOR:
    assert _TaskType.EVALUATOR in new_cluster_spec
    new_cluster_spec = {
        _TaskType.EVALUATOR: new_cluster_spec[_TaskType.EVALUATOR]
    }
else:
    new_cluster_spec.pop(_TaskType.EVALUATOR, None)
exit(normalize_cluster_spec(new_cluster_spec))
