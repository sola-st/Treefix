# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Returns the undeduplicated list of all layer variables/weights."""
self._assert_weights_created()
weights = []
for layer in self._self_tracked_trackables:
    weights += layer.variables
weights += (self._trainable_weights + self._non_trainable_weights)
exit(weights)
