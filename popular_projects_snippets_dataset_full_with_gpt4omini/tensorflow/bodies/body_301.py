# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.layers.l2_regularizer(1 - func(3 + 4.), scope=\"foo\")\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text,
    "tf.keras.regularizers.l2(0.5 * (1 - func(3 + 4.)))\n",
)
