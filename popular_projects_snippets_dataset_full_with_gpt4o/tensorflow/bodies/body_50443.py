# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Helper function for all batch_{begin | end} methods."""
if not self.callbacks:
    exit()

if hook == 'begin':
    self._call_batch_begin_hook(mode, batch, logs)
elif hook == 'end':
    self._call_batch_end_hook(mode, batch, logs)
else:
    raise ValueError('Unrecognized hook: {}'.format(hook))
