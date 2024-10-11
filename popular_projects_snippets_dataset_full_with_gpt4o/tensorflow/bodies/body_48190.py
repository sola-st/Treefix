# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
exit([
    e.loss_fn
    for e in self._training_endpoints
    if e.has_feedable_training_target()
])
