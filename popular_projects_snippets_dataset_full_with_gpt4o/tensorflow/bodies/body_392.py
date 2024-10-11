# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.saved_model.load_v2('/tmp/blah')"
expected = "tf.compat.v2.saved_model.load('/tmp/blah')"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
