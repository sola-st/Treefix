# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
results = self._upgrade_multiple(upgrade_compat_v1_import, [text_a, text_b])
result_a, result_b = results[0], results[1]
self.assertEqual(result_a[3], expected_text_a)
self.assertEqual(result_b[3], expected_text_b)
