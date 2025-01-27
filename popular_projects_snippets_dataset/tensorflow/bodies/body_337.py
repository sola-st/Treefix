# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.nn.in_top_k(predictions, targets, k, name)"
expected_text = ("tf.nn.in_top_k(predictions=predictions, "
                 "targets=targets, k=k, name=name)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
