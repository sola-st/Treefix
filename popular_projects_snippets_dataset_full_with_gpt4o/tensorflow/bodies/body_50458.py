# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Calls the `on_predict_batch_end` methods of its callbacks.

    Args:
        batch: Integer, index of batch within the current epoch.
        logs: Dict. Aggregated metric results up until this batch.
    """
if self._should_call_predict_batch_hooks:
    self._call_batch_hook(ModeKeys.PREDICT, 'end', batch, logs=logs)
