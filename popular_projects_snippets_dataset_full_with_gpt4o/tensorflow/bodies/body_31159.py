# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
h, c = state
exit((input_ + 1, (h + 1, c + 1)))
