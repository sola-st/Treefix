# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Initializes the TPUStrategy object.

    Args:
      tpu_cluster_resolver: A tf.distribute.cluster_resolver.TPUClusterResolver,
          which provides information about the TPU cluster.
      steps_per_run: Number of steps to run on device before returning to the
          host. Note that this can have side-effects on performance, hooks,
          metrics, summaries etc.
          This parameter is only used when Distribution Strategy is used with
          estimator or keras.
      device_assignment: Optional `tf.tpu.experimental.DeviceAssignment` to
          specify the placement of replicas on the TPU cluster. Currently only
          supports the usecase of using a single core within a TPU cluster.
    """
super(TPUStrategyV1, self).__init__(TPUExtended(
    self, tpu_cluster_resolver, steps_per_run, device_assignment))
distribute_lib.distribution_strategy_gauge.get_cell("V1").set("TPUStrategy")
distribute_lib.distribution_strategy_replica_gauge.get_cell(
    "num_workers").set(self.extended.num_hosts)
distribute_lib.distribution_strategy_replica_gauge.get_cell(
    "num_replicas_per_worker").set(self.extended.num_replicas_per_host)
# Packed variable is used to reduce the overhead of function execution.
# For a DistributedVariable, only one variable handle is captured into a
# function graph. It's only supported in eager mode.
self._enable_packed_variable_in_eager_mode = True
