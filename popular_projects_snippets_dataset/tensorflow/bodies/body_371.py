# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.summary.histogram('foo', myval, 'fam', 42)"
expected = ("tf.compat.v2.summary.histogram(name='foo', data=myval, "
            "step=42)")
_, _, errors, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
self.assertIn("'family' argument", errors[0])
self.assertIn("tf.compat.v2.summary.*", errors[1])
