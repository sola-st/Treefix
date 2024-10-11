# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
# TODO(b/137795644): This should return a PerReplica value but other
# methods like run in OneDeviceStrategy need to be modified
# to do the same.
exit(value_fn(distribute_lib.ValueContext()))
