# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "optimizer.minimize(a, foo=False)\n"
_, unused_report, errors, new_text = self._upgrade(text)
self.assertEqual(text, new_text)
self.assertEqual(errors, [])

text = "optimizer.minimize(a, colocate_gradients_with_ops=False)\n"
_, report, unused_errors, new_text = self._upgrade(text)
self.assertEqual("optimizer.minimize(a)\n", new_text)
self.assertIn("Optimizer.minimize no longer takes", report)
