# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.cond(a, b, c, True)"
expected_text = "tf.cond(pred=a, true_fn=b, false_fn=c)"
_, unused_report, errors, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
self.assertIn("tf.cond", errors[0])
self.assertIn("requires manual check", errors[0])
