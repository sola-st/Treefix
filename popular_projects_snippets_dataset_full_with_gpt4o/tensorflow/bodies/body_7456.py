# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py

device_list = [f'/{self.device_type}:{i}' for i in range(2)]
strategy = mirrored_strategy.MirroredStrategy(devices=device_list)
mesh = strategy._mesh
self.assertEqual(mesh.num_local_devices(), 2)
self.assertEqual(mesh.shape(), [2,])
self.assertEqual(mesh.dim_names, ['batch'])
self.assertIn(
    f'/job:localhost/replica:0/task:0/device:{self.device_type}:0',
    mesh.local_devices()[0])
self.assertIn(
    f'/job:localhost/replica:0/task:0/device:{self.device_type}:1',
    mesh.local_devices()[1])
