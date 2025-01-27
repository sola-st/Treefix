# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_test.py
_, unused_report, errors, new_text = self._upgrade(input)
self.assertEqual(new_text, output)
