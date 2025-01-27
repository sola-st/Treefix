# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
concatenated = array_ops.concat((input_, input_), axis=-1)
exit(((input_, concatenated), state + 1))
