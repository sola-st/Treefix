# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.framework.CriticalSection(shared_name='blah')"
expected = "tf.CriticalSection(shared_name='blah')"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
