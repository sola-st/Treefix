# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
for name in [
    "assert_greater", "assert_equal", "assert_none_equal", "assert_less",
    "assert_negative", "assert_positive", "assert_non_negative",
    "assert_non_positive", "assert_near", "assert_less",
    "assert_less_equal", "assert_greater", "assert_greater_equal",
    "assert_scalar"
]:
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
