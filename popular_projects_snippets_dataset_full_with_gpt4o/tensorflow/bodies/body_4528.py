# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data_test.py
model_settings = {
    "preprocess": "average",
}
features_min, _ = input_data.get_features_range(model_settings)
self.assertNear(0.0, features_min, 1e-5)
