# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
new_array = state[1].write(state[0], input_)
exit((input_, (state[0] + 1, new_array)))
