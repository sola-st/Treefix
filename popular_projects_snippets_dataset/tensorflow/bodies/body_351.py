# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
for name in ["assert_rank", "assert_rank_at_least", "assert_rank_in"]:
    text = "tf.%s(a)" % name
    expected_text = "tf.compat.v1.%s(a)" % name
    _, report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual(expected_text, new_text)
    self.assertIn("%s has been" % name, report)

    text = "tf.debugging.%s(a)" % name
    expected_text = "tf.compat.v1.debugging.%s(a)" % name
    _, report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual(expected_text, new_text)
    self.assertIn("%s has been" % name, report)
