# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.nn.dropout(x, keep_prob, name=\"foo\")\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text,
    "tf.nn.dropout(x, rate=1 - (keep_prob), name=\"foo\")\n",
)

text = "tf.nn.dropout(x, keep_prob=.4, name=\"foo\")\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text,
    "tf.nn.dropout(x, rate=1 - (.4), name=\"foo\")\n",
)

text = (
    "tf.nn.dropout(x,  # Stuff before\n"
    "              keep_prob=.4,  # Stuff after\n"
    "              name=\"foo\")\n"
)
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text,
    "tf.nn.dropout(x,  # Stuff before\n"
    "              rate=1 - (.4),  # Stuff after\n"
    "              name=\"foo\")\n",
)

text = "tf.nn.dropout(x)\n"
_, unused_report, errors, new_text = self._upgrade(text)
self.assertEqual(new_text, text)
self.assertIn("tf.nn.dropout called without arguments", errors[0])
