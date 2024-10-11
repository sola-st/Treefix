# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = (
    "tf.nn.softmax_cross_entropy_with_logits_v2("
    "labels=labels, logits=logits, dim=2)")
expected_text = (
    "tf.nn.softmax_cross_entropy_with_logits("
    "labels=labels, logits=logits, axis=2)")
_, unused_report, errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)

self.assertFalse(errors)
