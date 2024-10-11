# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
"""Configures the object.

    Args:
      session_config: a `tf.compat.v1.ConfigProto`
      cluster_spec: a dict, ClusterDef or ClusterSpec object specifying the
        cluster configurations.
      task_type: the current task type, such as "worker".
      task_id: the current task id.

    Raises:
      ValueError: if `task_type` is not in the `cluster_spec`.
    """
if cluster_spec:
    cluster_resolver = SimpleClusterResolver(
        cluster_spec=multi_worker_util.normalize_cluster_spec(cluster_spec),
        task_type=task_type,
        task_id=task_id,
        num_accelerators={
            self._local_device_type: self._num_devices_per_worker},
        rpc_layer=self._rpc_layer)
    self._initialize_multi_worker(cluster_resolver)
    assert isinstance(self._cross_device_ops,
                      cross_device_ops_lib.CollectiveAllReduce)

if session_config:
    session_config.CopyFrom(self._update_config_proto(session_config))
