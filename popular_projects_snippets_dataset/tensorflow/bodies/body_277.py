# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.boolean_mask(a, b, c, d)\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text,
                 "tf.boolean_mask(tensor=a, mask=b, name=c, axis=d)\n")
