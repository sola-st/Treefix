# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_type = rnn_cell_impl.DropoutWrapper
cell = rnn_cell_impl.BasicRNNCell(10)
wrapper = wrapper_type(cell)
# Github issue 15810
self.assertEqual(wrapper.wrapped_cell, cell)
self.assertEqual(wrapper.state_size, 10)
self.assertEqual(wrapper.output_size, 10)
