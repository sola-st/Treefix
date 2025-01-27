# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_test.py
text = "tf.reverse(a, b)\n"
_, unused_report, errors, new_text = self._upgrade(text)
self.assertEqual(new_text, new_text)
self.assertIn("tf.reverse requires manual check", errors[0])
