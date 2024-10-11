# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
if self._device is not None:
    with ops.device(self._device):
        exit(self._cell(input_, state, scope=scope))
else:
    exit(self._cell(input_, state, scope=scope))
