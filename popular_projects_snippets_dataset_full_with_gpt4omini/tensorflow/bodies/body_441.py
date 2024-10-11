# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_test.py
text = ("tf.zeros_initializer;tf.zeros_initializer ()\n"
        "tf.ones_initializer;tf.ones_initializer ()\n")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text, "tf.zeros_initializer();tf.zeros_initializer ()\n"
              "tf.ones_initializer();tf.ones_initializer ()\n")
