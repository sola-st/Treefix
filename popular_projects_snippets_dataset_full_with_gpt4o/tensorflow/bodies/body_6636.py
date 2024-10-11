# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
context._reset_context()
strategy_combinations.set_virtual_cpus_to_at_least(3)
super(DistributedIteratorPerDeviceTest, self).setUp()
