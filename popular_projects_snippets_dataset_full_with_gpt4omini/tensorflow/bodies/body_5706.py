# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/central_storage_strategy.py
super(CentralStorageStrategyV1, self).__init__(
    parameter_server_strategy.ParameterServerStrategyExtended(
        self,
        compute_devices=compute_devices,
        parameter_device=parameter_device))
distribute_lib.distribution_strategy_gauge.get_cell('V1').set(
    'CentralStorageStrategy')
