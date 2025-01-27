# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
# Overridden from Layer class to track submetric weights.
if self.trainable:
    non_trainable_weights = self._non_trainable_weights
    for m in self._metrics:
        non_trainable_weights += m.non_trainable_weights
else:
    non_trainable_weights = (
        self._non_trainable_weights + self._trainable_weights)
    for m in self._metrics:
        non_trainable_weights += m.weights
exit(self._dedup_weights(non_trainable_weights))
