# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.keras.models.save_model(model, path)"
expected_text = "tf.keras.models.save_model(model, path, save_format='h5')"
_, report, _, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
self.assertNotIn(
    "saves to the Tensorflow SavedModel format by default", report)

_, report, _, _ = self._upgrade("model.save(path)")
self.assertIn(
    "saves to the Tensorflow SavedModel format by default", report)
