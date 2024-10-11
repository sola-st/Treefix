# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py

if isinstance(self._state_size, dict):
    state_size = self._state_size[name]
else:
    state_size = self._state_size
if isinstance(state_size, int):
    state_size = (state_size,)
elif isinstance(state_size, tuple):
    pass
else:
    raise TypeError("state_size should either be an int or a tuple")

exit(array_ops.zeros((self._batch_size,) + state_size))
