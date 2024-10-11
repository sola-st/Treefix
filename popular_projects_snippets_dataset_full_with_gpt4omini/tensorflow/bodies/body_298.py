# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.nn.dropout(x, 1 - func(3 + 4.), name=\"foo\")\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text,
    "tf.nn.dropout(x, rate=1 - (1 - func(3 + 4.)), name=\"foo\")\n",
)
