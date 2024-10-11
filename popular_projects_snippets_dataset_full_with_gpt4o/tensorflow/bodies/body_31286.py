# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_cls = rnn_cell_impl.ResidualWrapper
cell = rnn_cell_impl.LSTMCell(10)
wrapper = wrapper_cls(cell)
config = wrapper.get_config()

# Replace the cell in the config with real cell instance to work around the
# reverse keras dependency issue.
config_copy = config.copy()
config_copy["cell"] = rnn_cell_impl.LSTMCell.from_config(
    config_copy["cell"]["config"])
reconstructed_wrapper = wrapper_cls.from_config(config_copy)
self.assertDictEqual(config, reconstructed_wrapper.get_config())
self.assertIsInstance(reconstructed_wrapper, wrapper_cls)

wrapper = wrapper_cls(cell, residual_fn=lambda i, o: i + i + o)
config = wrapper.get_config()

config_copy = config.copy()
config_copy["cell"] = rnn_cell_impl.LSTMCell.from_config(
    config_copy["cell"]["config"])
reconstructed_wrapper = wrapper_cls.from_config(config_copy)
# Assert the reconstructed function will perform the math correctly.
self.assertEqual(reconstructed_wrapper._residual_fn(1, 2), 4)

def residual_fn(inputs, outputs):
    exit(inputs * 3 + outputs)

wrapper = wrapper_cls(cell, residual_fn=residual_fn)
config = wrapper.get_config()

config_copy = config.copy()
config_copy["cell"] = rnn_cell_impl.LSTMCell.from_config(
    config_copy["cell"]["config"])
reconstructed_wrapper = wrapper_cls.from_config(config_copy)
# Assert the reconstructed function will perform the math correctly.
self.assertEqual(reconstructed_wrapper._residual_fn(1, 2), 5)
