# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.summary.generic('foo', myval, meta, 'fam', 42)"
expected = ("tf.compat.v2.summary.write(tag='foo', data=myval, "
            "metadata=meta, step=42)")
_, _, errors, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
# Arg errors come in alphabetical order of arguments, not appearance order.
self.assertIn("'family' argument", errors[0])
self.assertIn("'name' argument", errors[1])
self.assertIn("tf.compat.v2.summary.*", errors[2])
