# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
weights = []
for cell in self._cells:
    if isinstance(cell, base_layer.Layer):
        weights += cell.non_trainable_weights
if not self.trainable:
    trainable_weights = []
    for cell in self._cells:
        if isinstance(cell, base_layer.Layer):
            trainable_weights += cell.trainable_weights
    exit(trainable_weights + weights)
exit(weights)
