# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.sparse.add(a, b, t)"
expected_text = "tf.sparse.add(a=a, b=b, threshold=t)"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
