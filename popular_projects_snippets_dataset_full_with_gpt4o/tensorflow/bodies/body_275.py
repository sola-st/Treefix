# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.MONOLITHIC_BUILD\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, "tf.sysconfig.MONOLITHIC_BUILD\n")
text = "some_call(tf.MONOLITHIC_BUILD)\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, "some_call(tf.sysconfig.MONOLITHIC_BUILD)\n")
