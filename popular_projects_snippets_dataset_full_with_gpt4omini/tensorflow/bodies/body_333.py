# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.math.in_top_k(a, b, c, n)"
expected_text = (
    "tf.math.in_top_k(predictions=a, targets=b, k=c, name=n)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
