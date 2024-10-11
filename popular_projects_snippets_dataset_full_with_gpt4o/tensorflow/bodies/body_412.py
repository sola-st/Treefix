# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.keras.estimator.model_to_estimator(model)"
_, report, _, _ = self._upgrade(text)
expected_info = "will save object-based checkpoints"
self.assertIn(expected_info, report)
