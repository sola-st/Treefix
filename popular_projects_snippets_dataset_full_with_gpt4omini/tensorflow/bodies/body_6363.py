# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
"""Initializes the object."""
communication_options = collective_util.Options(
    implementation=communication)
super(CollectiveAllReduceStrategyV1, self).__init__(
    CollectiveAllReduceExtended(
        self,
        cluster_resolver=cluster_resolver,
        communication_options=communication_options))
distribute_lib.distribution_strategy_gauge.get_cell("V1").set(
    "MultiWorkerMirroredStrategy")
# pylint: disable=protected-access
distribute_lib.distribution_strategy_replica_gauge.get_cell(
    "num_workers").set(self.extended._num_workers)
distribute_lib.distribution_strategy_replica_gauge.get_cell(
    "num_gpu_per_worker").set(
        self.extended._num_devices_per_worker
        if self.extended._local_device_type == "GPU"
        else 0)
