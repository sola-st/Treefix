# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
extended = MirroredExtended(
    self, devices=devices, cross_device_ops=cross_device_ops)
super(MirroredStrategyV1, self).__init__(extended)
distribute_lib.distribution_strategy_gauge.get_cell("V1").set(
    "MirroredStrategy")
