# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Synchronous training in TPU donuts or Pods.

    Args:
      tpu_cluster_resolver: A
        `tf.distribute.cluster_resolver.TPUClusterResolver` instance, which
        provides information about the TPU cluster. If None, it will assume
        running on a local TPU worker.
      experimental_device_assignment: Optional
        `tf.tpu.experimental.DeviceAssignment` to specify the placement of
        replicas on the TPU cluster.
      experimental_spmd_xla_partitioning: If True, enable the SPMD (Single
        Program Multiple Data) mode in XLA compiler. This flag only affects the
        performance of XLA compilation and the HBM requirement of the compiled
        TPU program. Ceveat: if this flag is True, calling
        `tf.distribute.TPUStrategy.experimental_assign_to_logical_device` will
        result in a ValueError.
    """
super(TPUStrategyV2, self).__init__(
    TPUExtended(
        self,
        tpu_cluster_resolver,
        device_assignment=experimental_device_assignment,
        use_spmd_for_xla_partitioning=experimental_spmd_xla_partitioning))
distribute_lib.distribution_strategy_gauge.get_cell("V2").set("TPUStrategy")
distribute_lib.distribution_strategy_replica_gauge.get_cell(
    "num_workers").set(self.extended.num_hosts)
distribute_lib.distribution_strategy_replica_gauge.get_cell(
    "num_replicas_per_worker").set(self.extended.num_replicas_per_host)
# Packed variable is used to reduce the overhead of function execution.
# For a DistributedVariable, only one variable handle is captured into a
# function graph. It's only supported in eager mode.
# Packed variable is currently not supported when SPMD is enabled.
# TODO(b/202047549): enable Packed variable in SPMD mode.
self._enable_packed_variable_in_eager_mode = (
    not experimental_spmd_xla_partitioning)
