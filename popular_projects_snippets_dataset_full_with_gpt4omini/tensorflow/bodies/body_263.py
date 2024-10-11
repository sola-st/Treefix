# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.angle(a)\n"
_, report, unused_errors, unused_new_text = self._upgrade(text)
# This is not a complete test, but it is a sanity test that a report
# is generating information.
self.assertTrue(
    report.find("Renamed function `tf.angle` to "
                "`tf.math.angle`"))
