# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
strategy = mirrored_strategy.MirroredStrategy(["CPU:0", "GPU:0"])
self.assertIsInstance(
    strategy.extended._collective_ops,
    cross_device_ops_lib.ReductionToOneDevice)
