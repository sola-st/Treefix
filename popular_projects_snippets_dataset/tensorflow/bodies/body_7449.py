# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
strategy = mirrored_strategy.MirroredStrategy(self.mesh)
parameter_devices = strategy.extended.parameter_devices
self.assertLen(parameter_devices, 2)
self.assertEqual(parameter_devices, tuple(self.mesh.local_devices()))
