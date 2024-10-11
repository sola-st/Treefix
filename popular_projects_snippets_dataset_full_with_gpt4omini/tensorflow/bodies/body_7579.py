# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
"""Initialization of ParameterServerStrategyV2Extended."""
super(ParameterServerStrategyV2Extended, self).__init__(container_strategy)
self._num_ps = len(cluster_resolver.cluster_spec().as_dict().get("ps", []))
self._num_workers = len(cluster_resolver.cluster_spec().as_dict().get(
    "worker", []))
self._variable_count = 0

self._variable_partitioner = variable_partitioner
# The following two attrs are to verify that `ParameterServerStrategy`
# methods are properly used with a `ClusterCoordinator`.
self._used_with_coordinator = False
self._being_scheduled = False
self._set_num_gpus()
distribute_lib.distribution_strategy_replica_gauge.get_cell(
    "num_gpus_per_worker").set(self._num_gpus_per_worker)

# Don't canonicalize the devices here since this code is executed on Chief,
# but we want the reduce evaluation to be done on each worker. Placer will
# automatically choose the right device based on current context.
# TODO(ishark): Use select_cross_device_ops instead.
self._cross_device_ops = cross_device_ops_lib.ReductionToOneDevice(
    reduce_to_device="/device:CPU:0")
self._cross_device_ops._canonicalize_devices = False  # pylint: disable=protected-access
self._allow_run_without_coordinator = False
self._coordinator_creation_lock = threading.Lock()
