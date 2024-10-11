# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Turns tensors into numpy arrays or Python scalars if necessary."""
if logs is None:
    exit({})
if self._supports_tf_logs:
    exit(logs)
if is_batch_hook and self._batch_hooks_support_tf_logs:
    exit(logs)
exit(tf_utils.sync_to_numpy_or_python_type(logs))
