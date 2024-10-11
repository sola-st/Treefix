# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
"""Configures the strategy class with `cluster_spec`.

    The strategy object will be re-initialized if `cluster_spec` is passed to
    `configure` but was not passed when instantiating the strategy.

    Args:
      session_config: Session config object.
      cluster_spec: a dict, ClusterDef or ClusterSpec object specifying the
        cluster configurations.
      task_type: the current task type.
      task_id: the current task id.

    Raises:
      ValueError: if `cluster_spec` is given but `task_type` or `task_id` is
        not.
    """
if cluster_spec:
    # Use the num_gpus_per_worker recorded in constructor since _configure
    # doesn't take num_gpus.
    cluster_resolver = SimpleClusterResolver(
        cluster_spec=multi_worker_util.normalize_cluster_spec(cluster_spec),
        task_type=task_type,
        task_id=task_id,
        num_accelerators={"GPU": self._num_gpus_per_worker})
    self._initialize_multi_worker(cluster_resolver)

if session_config:
    session_config.CopyFrom(self._update_config_proto(session_config))
