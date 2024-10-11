# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
# Overridden from Layer class to track submetric weights.
if self.trainable:
    trainable_weights = self._trainable_weights
    for m in self._metrics:
        trainable_weights += m.trainable_weights
    exit(self._dedup_weights(trainable_weights))
else:
    exit([])
