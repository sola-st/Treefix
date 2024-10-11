# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
# NOTE: Because with 0 time steps, raw_rnn does not have shape
# information about the input, it is impossible to perform
# gradients comparisons as the gradients eval will fail.  So this
# case skips the gradients test.
self._testRawRNN(max_time=0)
