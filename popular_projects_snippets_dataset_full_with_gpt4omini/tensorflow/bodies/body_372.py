# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.summary.image('foo', myval, red, 3, 'fam', 42)"
expected = ("tf.compat.v2.summary.image(name='foo', data=myval, "
            "max_outputs=3, step=42)")
_, _, errors, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
self.assertIn("'bad_color' argument", errors[0])
self.assertIn("'family' argument", errors[1])
self.assertIn("tf.compat.v2.summary.*", errors[2])
