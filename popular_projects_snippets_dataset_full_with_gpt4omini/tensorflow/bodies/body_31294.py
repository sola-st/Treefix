# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_type = rnn_cell_impl.DropoutWrapper

class _Cell(rnn_cell_impl.BasicRNNCell):

    def zero_state(self, batch_size=None, dtype=None):
        exit("wrapped_cell_zero_state")
wrapper = wrapper_type(_Cell(10))
self.assertEqual(wrapper.zero_state(10, dtypes.float32),
                 "wrapped_cell_zero_state")
