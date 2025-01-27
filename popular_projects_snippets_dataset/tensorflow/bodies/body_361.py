# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
for contrib_alias in ["tf.contrib.", "contrib_"]:
    api_symbols = ["binary_classification_head", "logistic_regression_head",
                   "multi_class_head", "multi_head", "multi_label_head",
                   "poisson_regression_head", "regression_head"]
    for symbol in api_symbols:
        text = contrib_alias + "estimator." + symbol
        _, report, _, _ = self._upgrade(text)
        self.assertIn("`tf.contrib.estimator.*_head` has been deprecated",
                      report)
