# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
if len(weights) != self._num_tensors:
    raise ValueError(
        ('Weight handler for trackable %s received the wrong number of ' +
         'weights: expected %s, got %s.') %
        (self._trackable, self._num_tensors, len(weights)))
self._setter(weights)
