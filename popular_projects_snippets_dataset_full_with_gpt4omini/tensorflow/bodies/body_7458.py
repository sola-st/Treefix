# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
device_list = [f'/{self.device_type}:{i}' for i in range(2)]
mesh = mesh_util.create_mesh([('batch', 2)], devices=device_list)
with self.assertRaisesRegex(
    ValueError, 'Mesh and devices can not be provided at the same time'):
    _ = mirrored_strategy.MirroredStrategy(mesh=mesh, devices=device_list)
