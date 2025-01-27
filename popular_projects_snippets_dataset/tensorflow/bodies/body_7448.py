# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
strategy = mirrored_strategy.MirroredStrategy(self.mesh)
worker_devices = strategy.extended.worker_devices
self.assertLen(worker_devices, 2)
self.assertEqual(worker_devices, tuple(self.mesh.local_devices()))
