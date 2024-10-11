# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/mode_keys_test.py
with self.assertRaisesRegex(ValueError, 'Multiple keys/values found'):
    _ = mode_keys.ModeKeyMap(**{
        mode_keys.KerasModeKeys.PREDICT: 3,
        mode_keys.EstimatorModeKeys.PREDICT: 1
    })
