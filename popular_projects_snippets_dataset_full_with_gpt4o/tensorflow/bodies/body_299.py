# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.layers.l1_regularizer(scale)\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text,
    "tf.keras.regularizers.l1(scale)\n",
)
self.assertNotIn("Dropping scope", unused_report)

text = "tf.contrib.layers.l1_regularizer(scale, scope)\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text,
    "tf.keras.regularizers.l1(scale)\n",
)
self.assertIn("Dropping scope", unused_report)

text = (
    "slim.l1_regularizer(  # Stuff before\n"
    "                    scale=.4,"
    "                    scope=\"foo\")\n"
)
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text,
    "tf.keras.regularizers.l1(  # Stuff before\n"
    "                    l=.4)\n",
)
self.assertIn("Dropping scope", unused_report)
