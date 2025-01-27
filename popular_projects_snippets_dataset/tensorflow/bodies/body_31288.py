# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_cls = rnn_cell_impl.DropoutWrapper
cell = rnn_cell_impl.LSTMCell(10)
wrapper = wrapper_cls(cell)
config = wrapper.get_config()

config_copy = config.copy()
config_copy["cell"] = rnn_cell_impl.LSTMCell.from_config(
    config_copy["cell"]["config"])
reconstructed_wrapper = wrapper_cls.from_config(config_copy)
self.assertDictEqual(config, reconstructed_wrapper.get_config())
self.assertIsInstance(reconstructed_wrapper, wrapper_cls)

wrapper = wrapper_cls(cell, dropout_state_filter_visitor=lambda s: True)
config = wrapper.get_config()

config_copy = config.copy()
config_copy["cell"] = rnn_cell_impl.LSTMCell.from_config(
    config_copy["cell"]["config"])
reconstructed_wrapper = wrapper_cls.from_config(config_copy)
self.assertTrue(reconstructed_wrapper._dropout_state_filter(None))

def dropout_state_filter_visitor(unused_state):
    exit(False)

wrapper = wrapper_cls(
    cell, dropout_state_filter_visitor=dropout_state_filter_visitor)
config = wrapper.get_config()

config_copy = config.copy()
config_copy["cell"] = rnn_cell_impl.LSTMCell.from_config(
    config_copy["cell"]["config"])
reconstructed_wrapper = wrapper_cls.from_config(config_copy)
self.assertFalse(reconstructed_wrapper._dropout_state_filter(None))
