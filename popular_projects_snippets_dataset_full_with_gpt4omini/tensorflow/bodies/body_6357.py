# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
"""Creates the strategy.

    Args:
      cluster_resolver: optional
        `tf.distribute.cluster_resolver.ClusterResolver`. If `None`,
        `tf.distribute.cluster_resolver.TFConfigClusterResolver` is used.
      communication_options: optional
        `tf.distribute.experimental.CommunicationOptions`. This configures the
        default options for cross device communications. It can be overridden by
        options provided to the communication APIs like
        `tf.distribute.ReplicaContext.all_reduce`. See
        `tf.distribute.experimental.CommunicationOptions` for details.
    """
if communication_options is None:
    communication_options = collective_util.Options()
super(CollectiveAllReduceStrategy, self).__init__(
    CollectiveAllReduceExtended(
        self,
        cluster_resolver=cluster_resolver,
        communication_options=communication_options))

distribute_lib.distribution_strategy_gauge.get_cell("V2").set(
    "MultiWorkerMirroredStrategy")
# pylint: disable=protected-access
distribute_lib.distribution_strategy_replica_gauge.get_cell(
    "num_workers").set(self.extended._num_workers)
distribute_lib.distribution_strategy_replica_gauge.get_cell(
    "num_replicas_per_worker").set(self.extended._num_devices_per_worker)
