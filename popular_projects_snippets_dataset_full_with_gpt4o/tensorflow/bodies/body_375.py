# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.summary.audio('foo', myval, 44100)"
expected = ("tf.compat.v2.summary.audio(name='foo', data=myval, "
            "sample_rate=44100, "
            "step=tf.compat.v1.train.get_or_create_global_step())")
_, _, errors, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
self.assertIn("'step' argument", errors[0])
self.assertIn("tf.compat.v2.summary.*", errors[1])
