# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""One-time setup of loss objects."""
super(LossesContainer, self).build(y_pred)

self._losses = self._maybe_broadcast_to_outputs(y_pred, self._losses)
self._losses = self._conform_to_outputs(y_pred, self._losses)
self._losses = nest.map_structure(self._get_loss_object, self._losses)
self._losses = nest.flatten(self._losses)

self._loss_weights = self._maybe_broadcast_to_outputs(
    y_pred, self._loss_weights)
self._loss_weights = self._conform_to_outputs(y_pred, self._loss_weights)
self._loss_weights = nest.flatten(self._loss_weights)

self._create_metrics()
self._built = True
