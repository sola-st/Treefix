# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data_test.py
model_settings = {
    "preprocess": "mfcc",
}
features_min, features_max = input_data.get_features_range(model_settings)
self.assertLess(features_min, features_max)
