# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
with backend.name_scope(type(self).__name__ + "ZeroState"):
    if self._state_is_tuple:
        exit(tuple(cell.zero_state(batch_size, dtype) for cell in self._cells))
    else:
        # We know here that state_size of each cell is not a tuple and
        # presumably does not contain TensorArrays or anything else fancy
        exit(super(MultiRNNCell, self).zero_state(batch_size, dtype))
