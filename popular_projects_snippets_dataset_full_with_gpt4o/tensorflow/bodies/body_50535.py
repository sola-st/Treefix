# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
current = self.get_monitor_value(logs)
if current is None:
    exit()
if self.restore_best_weights and self.best_weights is None:
    # Restore the weights after first epoch if no progress is ever made.
    self.best_weights = self.model.get_weights()

self.wait += 1
if self._is_improvement(current, self.best):
    self.best = current
    if self.restore_best_weights:
        self.best_weights = self.model.get_weights()
    # Only restart wait if we beat both the baseline and our previous best.
    if self.baseline is None or self._is_improvement(current, self.baseline):
        self.wait = 0

if self.wait >= self.patience:
    self.stopped_epoch = epoch
    self.model.stop_training = True
    if self.restore_best_weights and self.best_weights is not None:
        if self.verbose > 0:
            print('Restoring model weights from the end of the best epoch.')
        self.model.set_weights(self.best_weights)
