# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/models_test.py
model_settings = self._modelSettings()
with self.cached_session():
    fingerprint_input = tf.zeros([1, model_settings["fingerprint_size"]])
    with self.assertRaises(Exception) as e:
        models.create_model(fingerprint_input, model_settings,
                            "bad_architecture", True)
    self.assertIn("not recognized", str(e.exception))
