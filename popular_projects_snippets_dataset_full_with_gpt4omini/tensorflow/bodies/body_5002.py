# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
"""Initialize the worker context object.

    Args:
      strategy: a `DistributionStrategy` object.
      cluster_spec: a ClusterSpec object. It can be empty or None in the local
        training case.
      task_type: a string indicating the role of the corresponding task, such as
        "worker" or "ps". It can be None if it is local training or in-graph
        replicated training.
      task_id: an integer indicating id of the corresponding task. It can be
        None if it is local training or in-graph replicated training.
      session_config: an optional `tf.compat.v1.ConfigProto` object.
      rpc_layer: optional string specifying the RPC protocol for communication
        with worker masters. If None or empty, hosts in the `cluster_spec` will
        be used directly.
      worker_barrier: optional, the barrier object for worker synchronization.
    """
self._strategy = strategy
self._cluster_spec = cluster_spec
self._task_type = task_type
self._task_id = task_id
self._session_config = session_config
self._worker_barrier = worker_barrier
self._rpc_layer = rpc_layer
self._master_target = self._get_master_target()
self._num_workers = _get_num_workers(cluster_spec)
self._is_chief_node = self._is_chief()
