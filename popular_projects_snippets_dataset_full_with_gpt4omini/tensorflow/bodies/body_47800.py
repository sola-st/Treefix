# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
if self._state_is_tuple:
    exit(tuple(cell.state_size for cell in self._cells))
else:
    exit(sum(cell.state_size for cell in self._cells))
