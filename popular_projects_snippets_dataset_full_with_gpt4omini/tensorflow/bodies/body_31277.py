# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
inp_sliced = array_ops.slice(inp, [0, 0], [-1, 3])
exit(inp_sliced + out)
