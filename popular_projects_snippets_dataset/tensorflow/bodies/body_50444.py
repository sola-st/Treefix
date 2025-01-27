# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Helper function for `on_*_batch_begin` methods."""
hook_name = 'on_{mode}_batch_begin'.format(mode=mode)
self._call_batch_hook_helper(hook_name, batch, logs)

if self._check_timing:
    self._batch_start_time = time.time()
