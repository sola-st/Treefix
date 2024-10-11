# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
super(ParameterServerStrategyExtended, self).__init__(container_strategy)
self._initialize_strategy(
    cluster_resolver=cluster_resolver,
    compute_devices=compute_devices,
    parameter_device=parameter_device)

# We typically don't need to do all-reduce in this strategy.
self._cross_device_ops = (
    cross_device_ops_lib.ReductionToOneDevice(reduce_to_device=_LOCAL_CPU))
