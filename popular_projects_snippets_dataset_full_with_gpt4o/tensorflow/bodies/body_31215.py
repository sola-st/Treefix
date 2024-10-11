# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
# Generate 2^5 option values
# from [True, True, True, True, True] to [False, False, False, False, False]
options = itertools.product([True, False], repeat=4)
for option in options:
    self._testBidirectionalDynamicRNN(
        use_shape=option[0],
        use_state_tuple=option[1],
        use_time_major=option[2],
        use_sequence_length=option[3])
