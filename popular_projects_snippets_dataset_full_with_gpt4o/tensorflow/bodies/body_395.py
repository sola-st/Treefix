# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.name_scope(None, default_name, [some, values])"
expected_text = "tf.name_scope(name=default_name)"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)

text = "tf.name_scope(default_name=default_name, values=stuff)"
expected_text = "tf.name_scope(name=default_name)"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)

text = "tf.name_scope(name=n, default_name=d, values=s)"
expected_text = "tf.compat.v1.name_scope(name=n, default_name=d, values=s)"
_, report, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
self.assertIn("`name` passed to `name_scope`", report)

text = "tf.name_scope(name=None, values=stuff)"
_, _, errors, _ = self._upgrade(text)
self.assertIn("name_scope call with neither name nor default_name",
              errors[0])
