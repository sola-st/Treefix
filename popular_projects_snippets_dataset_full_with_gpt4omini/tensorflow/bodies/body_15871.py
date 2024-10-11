# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex(TypeError, 'Not a _LayerBroadcaster'):
    dynamic_ragged_shape._get_layer_broadcasters_from_rps(int, [], [])
