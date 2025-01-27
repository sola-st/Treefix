# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_test.py
text = "tf.mul(a, b)\n"
_, report, unused_errors, unused_new_text = self._upgrade(text)
# This is not a complete test, but it is a sanity test that a report
# is generating information.
self.assertTrue(report.find("Renamed function `tf.mul` to `tf.multiply`"))
