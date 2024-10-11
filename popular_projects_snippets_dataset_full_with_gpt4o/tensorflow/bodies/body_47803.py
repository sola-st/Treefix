# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
if not self.trainable:
    exit([])
weights = []
for cell in self._cells:
    if isinstance(cell, base_layer.Layer):
        weights += cell.trainable_weights
exit(weights)
