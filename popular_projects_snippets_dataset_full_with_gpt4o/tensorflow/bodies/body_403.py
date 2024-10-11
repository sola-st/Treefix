# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.pywrap_tensorflow.foo()"
expected = "tf.pywrap_tensorflow.foo()"
_, _, errors, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
self.assertIn("`tf.pywrap_tensorflow` will not be distributed", errors[0])
