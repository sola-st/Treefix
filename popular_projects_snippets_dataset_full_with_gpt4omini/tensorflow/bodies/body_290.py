# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
classes = [
    "BaselineClassifier", "BaselineRegressor", "LinearClassifier",
    "LinearRegressor", "DNNRegressor", "DNNClassifier"
]

for c in classes:
    ns = "tf.estimator." + c
    suffix = "(optimizer=TEST)"
    text = ns + suffix
    suffix = ("(optimizer=TEST, "
              "loss_reduction=tf.keras.losses.Reduction.SUM)")
    expected_text = "tf.compat.v1.estimator." + c + suffix
    _, unused_report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual(new_text, expected_text)
