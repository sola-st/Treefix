# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
"""Run the cell on specified device."""
with ops.device(self._device):
    exit(cell_call_fn(inputs, state, **kwargs))
