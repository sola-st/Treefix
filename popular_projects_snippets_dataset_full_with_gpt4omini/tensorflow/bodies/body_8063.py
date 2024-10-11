# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
super().setUp()
if context.context().list_physical_devices('TPU'):
    self.skipTest('Test not supported on TPUs')
