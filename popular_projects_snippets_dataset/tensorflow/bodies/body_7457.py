# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
strategy = mirrored_strategy.MirroredStrategy()
mesh = strategy._mesh
self.assertEqual(mesh.num_local_devices(), 2)
self.assertEqual(mesh.shape(), [2,])
self.assertIn(
    f'/job:localhost/replica:0/task:0/device:{self.device_type}:0',
    mesh.local_devices()[0])
self.assertIn(
    f'/job:localhost/replica:0/task:0/device:{self.device_type}:1',
    mesh.local_devices()[1])
