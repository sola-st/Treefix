# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.estimator.inputs.numpy_input_fn(0)"
expected_text = "tf.compat.v1.estimator.inputs.numpy_input_fn(0)"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)

text = "tf.estimator.inputs.pandas_input_fn(0)"
expected_text = "tf.compat.v1.estimator.inputs.pandas_input_fn(0)"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
