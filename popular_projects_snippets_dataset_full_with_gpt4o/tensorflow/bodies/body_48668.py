# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
super(LossesContainer, self).__init__(output_names=output_names)

# Keep user-supplied values untouched for recompiling and serialization.
self._user_losses = losses
self._user_loss_weights = loss_weights

self._losses = losses
self._loss_weights = loss_weights
self._per_output_metrics = None  # Per-output losses become metrics.
self._loss_metric = metrics_mod.Mean(name='loss')  # Total loss.
self._built = False
