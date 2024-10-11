# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
state = root.cell.zero_state(3, dtype=x.dtype)
y, _ = root.cell(x, state)
exit(y)
