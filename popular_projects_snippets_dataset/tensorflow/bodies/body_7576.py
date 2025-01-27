# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
"""Initializes the TF2 parameter server strategy.

    This initializes the `tf.distribute.experimental.ParameterServerStrategy`
    object to be ready for use with
    `tf.distribute.experimental.coordinator.ClusterCoordinator`.

    Args:
      cluster_resolver: a `tf.distribute.cluster_resolver.ClusterResolver`
        object.
      variable_partitioner:
        a `distribute.experimental.partitioners.Partitioner` that specifies
        how to partition variables. If `None`, variables will not be
        partitioned.

        * Predefined partitioners in `tf.distribute.experimental.partitioners`
        can be used for this argument. A commonly used partitioner is
        `MinSizePartitioner(min_shard_bytes = 256 << 10, max_shards = num_ps)`,
        which allocates at least 256K per shard, and each ps gets at most one
        shard.

        * `variable_partitioner` will be called for each variable created under
        strategy `scope` to instruct how the variable should be partitioned.
        Variables that have only one partition along the partitioning axis
        (i.e., no need for partition) will be created as a normal `tf.Variable`.

        * Only the first / outermost axis partitioning is supported.

        * Div partition strategy is used to partition variables. Assuming we
        assign consecutive integer ids along the first axis of a variable, then
        ids are assigned to shards in a contiguous manner, while attempting to
        keep each shard size identical. If the ids do not evenly divide the
        number of shards, each of the first several shards will be assigned one
        more id. For instance, a variable whose first dimension is 13 has 13
        ids, and they are split across 5 shards as:
        `[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10], [11, 12]]`.

        * Variables created under `strategy.extended.colocate_vars_with` will
        not be partitioned.
    """
# pyformat: enable
self._cluster_resolver = cluster_resolver

self._verify_args_and_config(cluster_resolver)
self._cluster_coordinator = None
logging.info(
    "`tf.distribute.experimental.ParameterServerStrategy` is initialized "
    "with cluster_spec: %s", cluster_resolver.cluster_spec())

# TODO(b/167894802): Make coordinator, worker, and ps names customizable.
self._connect_to_cluster(coordinator_name="chief")
self._extended = ParameterServerStrategyV2Extended(self, cluster_resolver,
                                                   variable_partitioner)
super(ParameterServerStrategyV2, self).__init__(self._extended)
distribute_lib.distribution_strategy_gauge.get_cell("V2").set(
    "ParameterServerStrategy")
self._should_use_with_coordinator = True
# Used while constructing distributed iterators.
self._canonicalize_devices = False
