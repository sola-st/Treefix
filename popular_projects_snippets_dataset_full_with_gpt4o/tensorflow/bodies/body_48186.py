# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""The output target tensors for the model."""
exit([
    e.training_target.target
    for e in self._training_endpoints
    if e.has_training_target()
])
