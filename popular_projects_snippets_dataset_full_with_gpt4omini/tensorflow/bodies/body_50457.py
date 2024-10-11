# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Calls the `on_predict_batch_begin` methods of its callbacks.

    Args:
        batch: Integer, index of batch within the current epoch.
        logs: Dict, contains the return value of `model.predict_step`,
          it typically returns a dict with a key 'outputs' containing
          the model's outputs.
    """
if self._should_call_predict_batch_hooks:
    self._call_batch_hook(ModeKeys.PREDICT, 'begin', batch, logs=logs)
