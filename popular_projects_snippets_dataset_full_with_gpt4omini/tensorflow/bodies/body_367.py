# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
api_symbols = ["RNNCell", "BasicLSTMCell", "BasicRNNCell", "GRUCell",
               "LSTMCell", "MultiRNNCell"]
for symbol in api_symbols:
    text = "tf.contrib.rnn." + symbol
    expected_text = "tf.compat.v1.nn.rnn_cell." + symbol
    _, _, _, new_text = self._upgrade(text)
    self.assertEqual(expected_text, new_text)
