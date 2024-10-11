# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Synchronous training in TPU donuts or Pods.

    Args:
      tpu_cluster_resolver: A tf.distribute.cluster_resolver.TPUClusterResolver,
        which provides information about the TPU cluster.
      device_assignment: Optional `tf.tpu.experimental.DeviceAssignment` to
        specify the placement of replicas on the TPU cluster.
    """
logging.warning(
    "`tf.distribute.experimental.TPUStrategy` is deprecated, please use "
    " the non experimental symbol `tf.distribute.TPUStrategy` instead.")

super(TPUStrategy, self).__init__(
    TPUExtended(
        self, tpu_cluster_resolver, device_assignment=device_assignment))
distribute_lib.distribution_strategy_gauge.get_cell("V2").set("TPUStrategy")
distribute_lib.distribution_strategy_replica_gauge.get_cell(
    "num_workers").set(self.extended.num_hosts)
distribute_lib.distribution_strategy_replica_gauge.get_cell(
    "num_replicas_per_worker").set(self.extended.num_replicas_per_host)
# Packed variable is used to reduce the overhead of function execution.
# For a DistributedVariable, only one variable handle is captured into a
# function graph. It's only supported in eager mode.
self._enable_packed_variable_in_eager_mode = True
