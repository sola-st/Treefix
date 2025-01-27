# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/models_test.py
model_settings = self._modelSettings()
with self.cached_session() as sess:
    fingerprint_input = tf.zeros([1, model_settings["fingerprint_size"]])
    logits = models.create_model(fingerprint_input, model_settings, "conv",
                                 False)
    self.assertIsNotNone(logits)
    self.assertIsNotNone(sess.graph.get_tensor_by_name(logits.name))
