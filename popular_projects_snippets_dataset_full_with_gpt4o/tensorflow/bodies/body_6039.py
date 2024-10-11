# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
super(OneDeviceStrategyV1, self).__init__(OneDeviceExtended(self, device))
distribute_lib.distribution_strategy_gauge.get_cell("V1").set(
    "OneDeviceStrategy")
