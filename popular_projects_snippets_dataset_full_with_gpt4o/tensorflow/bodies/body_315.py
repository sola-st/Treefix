# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.autograph.to_graph(f, True, arg_values=None, arg_types=None)"
expected_text = "tf.autograph.to_graph(f, True)"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)

text = ("tf.autograph.to_code"
        "(f, False, arg_values=None, arg_types=None, indentation=' ')")
expected_text = "tf.autograph.to_code(f, False)"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
