# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
api_symbols = ["static_rnn", "static_state_saving_rnn",
               "static_bidirectional_rnn"]
for symbol in api_symbols:
    text = "tf.contrib.rnn." + symbol
    expected_text = "tf.compat.v1.nn." + symbol
    _, _, _, new_text = self._upgrade(text)
    self.assertEqual(expected_text, new_text)
