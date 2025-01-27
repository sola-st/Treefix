# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
classes = ["DNNLinearCombinedEstimator"]
for c in classes:
    ns = "tf.estimator." + c
    suffix = ("(input_layer_partitioner=TEST, dnn_optimizer=TEST, "
              "linear_optimizer=TEST)")
    text = ns + suffix
    expected_text = "tf.compat.v1.estimator." + c + suffix
    _, unused_report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual(new_text, expected_text)
