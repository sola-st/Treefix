# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Calls the `on_epoch_end` methods of its callbacks.

    This function should only be called during TRAIN mode.

    Args:
        epoch: Integer, index of epoch.
        logs: Dict, metric results for this training epoch, and for the
          validation epoch if validation is performed. Validation result keys
          are prefixed with `val_`.
    """
logs = self._process_logs(logs)
for callback in self.callbacks:
    callback.on_epoch_end(epoch, logs)
