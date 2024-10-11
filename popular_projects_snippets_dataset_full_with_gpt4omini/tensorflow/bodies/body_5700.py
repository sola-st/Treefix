# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/central_storage_strategy.py
extended = parameter_server_strategy.ParameterServerStrategyExtended(
    self,
    compute_devices=compute_devices,
    parameter_device=parameter_device)
"""Initializes the strategy with optional device strings.

    Args:
    compute_devices: an optional list of strings for device to replicate models
      on. If this is not provided, all local GPUs will be used; if there is no
      GPU, local CPU will be used.
    parameter_device: an optional device string for which device to put
      variables on. The default one is CPU or GPU if there is only one.
    """
super(CentralStorageStrategy, self).__init__(extended)
distribute_lib.distribution_strategy_gauge.get_cell('V2').set(
    'CentralStorageStrategy')
