# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
super(TestStateSaverWithCounters, self).__init__(batch_size, state_size)
self._num_state_calls = variables_lib.VariableV1(0)
self._num_save_state_calls = variables_lib.VariableV1(0)
