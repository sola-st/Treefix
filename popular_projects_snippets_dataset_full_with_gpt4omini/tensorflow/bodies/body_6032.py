# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
"""Creates a `OneDeviceStrategy`.

    Args:
      device: Device string identifier for the device on which the variables
        should be placed. See class docs for more details on how the device is
        used. Examples: "/cpu:0", "/gpu:0", "/device:CPU:0", "/device:GPU:0"
    """
super(OneDeviceStrategy, self).__init__(OneDeviceExtended(self, device))
distribute_lib.distribution_strategy_gauge.get_cell("V2").set(
    "OneDeviceStrategy")
