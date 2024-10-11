# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
exit((LSTMStateTuple(self._num_units, self._num_units)
        if self._state_is_tuple else 2 * self._num_units))
