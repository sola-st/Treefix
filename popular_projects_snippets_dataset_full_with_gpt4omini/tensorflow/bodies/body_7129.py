# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
strategy = mirrored_strategy.MirroredStrategy(["CPU:0", "CPU:1"])
self.assertEqual(
    strategy.extended._collective_ops._options.implementation,
    collective_util.CommunicationImplementation.RING)
