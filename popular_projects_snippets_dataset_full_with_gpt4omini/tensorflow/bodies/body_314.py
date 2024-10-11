# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.argmax(input, name=n, dimension=1, output_type=type)"
expected_text = "tf.argmax(input=input, name=n, axis=1, output_type=type)"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)

text = "tf.argmax(input, 0)"
expected_text = "tf.argmax(input=input, axis=0)"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)

text = "tf.arg_max(input, 0)"
expected_text = "tf.argmax(input, 0)"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
