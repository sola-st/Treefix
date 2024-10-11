# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.xla.experimental.jit_scope(0)"
expected_text = "tf.xla.experimental.jit_scope(0)"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)

text = "tf.xla.experimental.compile(0)"
expected_text = "tf.xla.experimental.compile(0)"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
