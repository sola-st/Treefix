# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
strategy = mirrored_strategy.MirroredStrategy(["GPU:0", "GPU:1", "GPU:2"])
self.assertEqual(
    strategy.extended._collective_ops._options.implementation,
    collective_util.CommunicationImplementation.RING)
