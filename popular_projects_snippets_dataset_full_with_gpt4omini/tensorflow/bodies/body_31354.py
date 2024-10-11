# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
f32 = dtypes.float32
f64 = dtypes.float64
self._assert_cell_builds(rnn_cell_impl.BasicRNNCell, f32, 5, 7, 3)
self._assert_cell_builds(rnn_cell_impl.BasicRNNCell, f64, 5, 7, 3)
self._assert_cell_builds(rnn_cell_impl.BasicLSTMCell, f32, 5, 7, 3)
self._assert_cell_builds(rnn_cell_impl.BasicLSTMCell, f64, 5, 7, 3)
self._assert_cell_builds(rnn_cell_impl.GRUCell, f32, 5, 7, 3)
self._assert_cell_builds(rnn_cell_impl.GRUCell, f64, 5, 7, 3)
self._assert_cell_builds(rnn_cell_impl.LSTMCell, f32, 5, 7, 3)
self._assert_cell_builds(rnn_cell_impl.LSTMCell, f64, 5, 7, 3)
