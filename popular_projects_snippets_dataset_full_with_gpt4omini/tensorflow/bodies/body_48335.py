# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Set `trainable` state for each sublayer."""
if self in trainable_state:
    self.trainable = trainable_state[self]
layers = self._flatten_layers(include_self=False, recursive=False)
for l in layers:
    if l in trainable_state:
        l._set_trainable_state(trainable_state)
