# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/estimator_training.py
"""Initializes run config from distribute coordinator's worker context."""

# pylint: disable=protected-access
config._service = None
config._cluster_spec = worker_context.cluster_spec
config._task_type = worker_context.task_type
config._task_id = worker_context.task_id
config._evaluation_master = worker_context.master_target
config._master = worker_context.master_target
config._is_chief = worker_context.is_chief

if config._cluster_spec:
    # Distributed mode.
    if config._task_type != EVALUATOR:

        config._num_ps_replicas = _count_ps(config._cluster_spec)
        config._num_worker_replicas = _count_worker(
            config._cluster_spec, chief_task_type=CHIEF)
        config._global_id_in_cluster = _get_global_id(
            config._cluster_spec,
            config._task_type,
            config._task_id,
            chief_task_type=CHIEF)
    else:
        # Evaluator task should not be aware of the other tasks.
        config._cluster_spec = server_lib.ClusterSpec({})
        config._num_ps_replicas = 0
        config._num_worker_replicas = 0
        config._global_id_in_cluster = None  # undefined
else:
    # Local mode.
    config._global_id_in_cluster = 0
    config._num_ps_replicas = 0
    config._num_worker_replicas = 1
