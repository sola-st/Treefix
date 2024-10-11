# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.gradients(yx=a, foo=False)\n"
_, unused_report, errors, new_text = self._upgrade(text)
self.assertEqual(text, new_text)
self.assertEqual(errors, [])

text = "tf.gradients(yx=a, colocate_gradients_with_ops=False)\n"
_, report, unused_errors, new_text = self._upgrade(text)
self.assertEqual("tf.gradients(yx=a)\n", new_text)
self.assertIn("tf.gradients no longer takes", report)

text = "tf.gradients(y, x, grad_ys, name, colocate, gate)\n"
expected = ("tf.gradients(ys=y, xs=x, grad_ys=grad_ys, name=name, "
            "gate_gradients=gate)\n")
_, unused_report, errors, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
