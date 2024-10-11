# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
if not cluster_resolver.cluster_spec():
    raise ValueError("Cluster spec must be non-empty in "
                     "`tf.distribute.cluster_resolver.ClusterResolver`.")
cluster_spec = cluster_resolver.cluster_spec()

# The following checks if the task types are allowed (chief, ps, worker).
multi_worker_util._validate_cluster_spec(  # pylint: disable=protected-access
    cluster_spec, cluster_resolver.task_type, cluster_resolver.task_id)

if multi_worker_util.task_count(cluster_spec, "ps") < 1:
    raise ValueError("There must be at least one ps.")

if multi_worker_util.task_count(cluster_spec, "worker") < 1:
    raise ValueError("There must be at least one worker.")
