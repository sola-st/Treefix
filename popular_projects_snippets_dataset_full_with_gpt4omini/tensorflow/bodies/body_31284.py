# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_cls = rnn_cell_impl.DeviceWrapper
cell = rnn_cell_impl.LSTMCell(10)
wrapper = wrapper_cls(cell, "/cpu:0")
config = wrapper.get_config()

# Replace the cell in the config with real cell instance to work around the
# reverse keras dependency issue.
config_copy = config.copy()
config_copy["cell"] = rnn_cell_impl.LSTMCell.from_config(
    config_copy["cell"]["config"])
reconstructed_wrapper = wrapper_cls.from_config(config_copy)
self.assertDictEqual(config, reconstructed_wrapper.get_config())
self.assertIsInstance(reconstructed_wrapper, wrapper_cls)
