# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.hessians(ys=a, xs=b, colocate_gradients_with_ops=False)\n"
_, report, unused_errors, new_text = self._upgrade(text)
self.assertEqual("tf.hessians(ys=a, xs=b)\n", new_text)
self.assertIn("tf.hessians no longer takes", report)
