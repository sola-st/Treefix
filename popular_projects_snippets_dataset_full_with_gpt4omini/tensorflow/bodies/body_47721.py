# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
with ops.name_scope_v2(type(self).__name__ + "ZeroState"):
    exit(self.cell.zero_state(batch_size, dtype))
