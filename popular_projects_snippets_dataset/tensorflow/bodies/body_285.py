# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
classes = [
    "LinearClassifier", "LinearRegressor", "DNNLinearCombinedClassifier",
    "DNNLinearCombinedRegressor", "DNNRegressor", "DNNClassifier",
    "BaselineClassifier", "BaselineRegressor"
]
for c in classes:
    ns = "tf.estimator." + c
    text = ns + "()"
    expected_text = ns + "(loss_reduction=tf.keras.losses.Reduction.SUM)"
    _, report, errors, new_text = self._upgrade(text)
    self.assertEqual(expected_text, new_text)

    text = ns + "(loss_reduction=TEST)"
    expected_text = ns + "(loss_reduction=TEST)"
    _, report, errors, new_text = self._upgrade(text)
    self.assertEqual(text, new_text)
text = "tf.estimator.BaselineClassifier(m, c, w, v, o, c, lr)"
expected_text = (
    "tf.compat.v1.estimator.BaselineClassifier("
    "model_dir=m, n_classes=c, weight_column=w, label_vocabulary=v, "
    "optimizer=o, config=c, loss_reduction=lr)")
_, report, errors, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)

text = "tf.estimator.BaselineClassifier(model_dir=model_dir)"
expected_text = ("tf.estimator.BaselineClassifier(" +
                 "model_dir=model_dir, "
                 "loss_reduction=tf.keras.losses.Reduction.SUM)")
_, report, errors, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
