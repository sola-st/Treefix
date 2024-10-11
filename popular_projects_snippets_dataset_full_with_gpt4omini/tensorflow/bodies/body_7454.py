# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
with self.assertRaisesRegex(
    ValueError, 'The mesh for MirroredStrategy must be 1D, received: 2D'):
    mirrored_strategy.MirroredStrategy(self.mesh_2d)
