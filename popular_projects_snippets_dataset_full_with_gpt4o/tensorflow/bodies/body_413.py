# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.keras.experimental.export_saved_model"
_, report, _, _ = self._upgrade(text)
expected_info = "Please use model.save"
self.assertIn(expected_info, report)
