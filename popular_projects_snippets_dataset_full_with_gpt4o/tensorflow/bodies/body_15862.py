# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
bad_gather_index = constant_op.constant([0.0, 0.5, 1.0])
with self.assertRaisesRegex(ValueError, 'gather_index must be'):
    _LayerBroadcaster.from_gather_index(bad_gather_index)
