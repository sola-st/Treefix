# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
classes = [
    "LinearClassifier", "LinearRegressor", "DNNLinearCombinedClassifier",
    "DNNLinearCombinedRegressor", "DNNRegressor", "DNNClassifier"
]

for c in classes:
    ns = "tf.estimator." + c
    suffix = "(input_layer_partitioner=TEST)"
    text = ns + suffix
    suffix = ("(input_layer_partitioner=TEST, "
              "loss_reduction=tf.keras.losses.Reduction.SUM)")
    expected_text = "tf.compat.v1.estimator." + c + suffix
    _, unused_report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual(new_text, expected_text)
