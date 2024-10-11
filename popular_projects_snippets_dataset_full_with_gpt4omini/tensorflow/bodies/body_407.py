# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.layers.recompute_grad()"
expected = "tf.recompute_grad()"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
