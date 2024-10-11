# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = (
    "tf.contrib.saved_model.save_keras_model(model, './saved_models')\n"
    "tf.contrib.saved_model.load_keras_model(saved_model_path)\n")
expected_text = (
    "tf.compat.v1.keras.experimental.export_saved_model(model, "
    "'./saved_models')\ntf.compat.v1.keras.experimental."
    "load_from_saved_model(saved_model_path)\n"
)
_, report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
expected_info = "Please use model.save"
self.assertIn(expected_info, report)
