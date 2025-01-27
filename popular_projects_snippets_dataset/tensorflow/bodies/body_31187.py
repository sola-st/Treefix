# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
exit(rnn_cell.LSTMCell(
    num_units + i,
    use_peepholes=False,
    initializer=initializer,
    state_is_tuple=True))
