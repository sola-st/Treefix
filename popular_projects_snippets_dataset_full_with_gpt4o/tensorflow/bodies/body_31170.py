# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
with ops.control_dependencies([state_ops.assign_add(
    self._num_save_state_calls, 1)]):
    exit(super(TestStateSaverWithCounters, self).save_state(name, state))
