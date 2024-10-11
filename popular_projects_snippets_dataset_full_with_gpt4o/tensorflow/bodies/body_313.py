# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.argmin(input, name=n, dimension=1, output_type=type)"
expected_text = "tf.argmin(input=input, name=n, axis=1, output_type=type)"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)

text = "tf.argmin(input, 0)"
expected_text = "tf.argmin(input=input, axis=0)"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)

text = "tf.arg_min(input, 0)"
expected_text = "tf.argmin(input, 0)"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
