# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/mode_keys_test.py
mode_map = mode_keys.ModeKeyMap(**{
    mode_keys.KerasModeKeys.PREDICT: 3,
    mode_keys.KerasModeKeys.TEST: 1
})

# Test dictionary __getitem__
self.assertEqual(3, mode_map[mode_keys.KerasModeKeys.PREDICT])
self.assertEqual(3, mode_map[mode_keys.EstimatorModeKeys.PREDICT])
self.assertEqual(1, mode_map[mode_keys.KerasModeKeys.TEST])
self.assertEqual(1, mode_map[mode_keys.EstimatorModeKeys.EVAL])
with self.assertRaises(KeyError):
    _ = mode_map[mode_keys.KerasModeKeys.TRAIN]
with self.assertRaises(KeyError):
    _ = mode_map[mode_keys.EstimatorModeKeys.TRAIN]
with self.assertRaisesRegex(ValueError, 'Invalid mode'):
    _ = mode_map['serve']

# Test common dictionary methods
self.assertLen(mode_map, 2)
self.assertEqual({1, 3}, set(mode_map.values()))
self.assertEqual(
    {mode_keys.KerasModeKeys.TEST, mode_keys.KerasModeKeys.PREDICT},
    set(mode_map.keys()))

# Map is immutable
with self.assertRaises(TypeError):
    mode_map[mode_keys.KerasModeKeys.TEST] = 1  # pylint: disable=unsupported-assignment-operation
